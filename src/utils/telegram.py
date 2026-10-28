import hmac
import hashlib
import time
import json
from urllib.parse import parse_qs, unquote
from django.conf import settings


MAX_AGE = 300 # seconds



def parse_init_data(init_data: str) -> dict | None:
    try:
        # Parse init_data
        parsed = parse_qs(init_data, keep_blank_values=True)
        received_hash = parsed.pop('hash', [None])[0]

        if not received_hash:
            return None

        auth_date = parsed.get('auth_date', [None])[0]
        if not auth_date:
            None

        current_time = int(time.time())
        auth_timestamp = int(auth_date)

        if current_time - auth_timestamp > MAX_AGE:
            return None

        # Create data-check-string
        data_check_arr = [f"{k}={unquote(v[0])}" for k, v in sorted(parsed.items())]
        data_check_string = '\n'.join(data_check_arr)

        # HMAC-SHA256 verify
        secret = hmac.new(
            key=b"WebAppData",
            msg=settings.BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()

        expected = hmac.new(
            key=secret,
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(expected, received_hash):
            return None

        # Parse user object
        raw_user = json.loads(unquote(parsed.get("user", ["{}"])[0]))
        first = raw_user.get("first_name", "")
        last = raw_user.get("last_name", "")

        return {
            "telegram_id": raw_user["id"],
            "full_name": f"{first} {last}".strip(),
            "photo_url": raw_user.get("photo_url"),
        }


    except Exception as e:
        print(f"parse_init_data error: {e}")
        return None
