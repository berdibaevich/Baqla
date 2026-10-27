import hmac
import hashlib
import time
from urllib.parse import parse_qs, unquote
from django.conf import settings


MAX_AGE_SECONDS = 300 # 5 minutes



def verify_init_data(init_data: str) -> dict:
    try:
        # Parse init_data
        parsed = parse_qs(init_data)
        received_hash = parsed.pop('hash', [None])[0]

        if not received_hash:
            return {
                'valid': False, 
                'message': 'Ошибка авторизации. Пожалуйста, запустите приложение заново из Telegram.'
            }

        auth_date = parsed.get('auth_date', [None])[0]
        if not auth_date:
            return {
                'valid': False,
                'message': 'Данные авторизации неполные.'
            }

        current_time = int(time.time())
        auth_timestamp = int(auth_date)

        if current_time - auth_timestamp > MAX_AGE_SECONDS:
            return {
                'valid': False,
                'message': 'Сессия истекла. Пожалуйста, перезапустите приложение.'
            }

        # Create data-check-string
        data_check_arr = [f"{k}={unquote(v[0])}" for k, v in sorted(parsed.items())]
        data_check_string = '\n'.join(data_check_arr)

        # Secret key = HMAC-SHA-256(BOT_TOKEN, "WebAppData")

        secret_key = hmac.new(
            key=b"WebAppData",
            msg=settings.BOT_TOKEN.encode(),
            digestmod=hashlib.sha256
        ).digest()

        calculated_hash = hmac.new(
            key=secret_key,
            msg=data_check_string.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()


        if calculated_hash != received_hash:
            return {
                'valid': False,
                'message': 'Не удалось подтвердить безопасность сессии. Перезапустите приложение.'
            }

        return {'valid': True, 'message': 'Ok'}


    except Exception as e:
        print(f"Verify init data error: {e}")
        return {
            'valid': False, 
            'message': 'Maǵliwmatlardi tekseriwdegi texnikaliq qáte. Keyinirek qayta uriniń.'
        }

