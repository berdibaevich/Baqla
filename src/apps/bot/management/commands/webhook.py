"""
    - Telegram webhook management command.

    python manage.py webhook --set
    python manage.py webhook --info
    python manage.py webhook --delete
"""

import httpx
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    help = "Telegram webhook: --set | --info | --delete"

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--set", action="store_true", help="Set webhook")
        group.add_argument("--info", action="store_true", help="Get webhook info")
        group.add_argument("--delete", action="store_true", help="Delete webhook")


    def handle(self, *args, **options):
        token = settings.BOT_TOKEN
        domain = settings.WEBHOOK_HOST

        base_url = f"https://api.telegram.org/bot{token}"

        if options["set"]:
            self._set(base_url=base_url, token=token, domain=domain)


    def _set(self, base_url: str, token: str, domain: str) -> None:
        webhook_url = f"{domain}/webhook/{token}/"

        r = self._request(
            f"{base_url}/setWebhook",
            params={
                "url": webhook_url,
                "allowed_updates": ["message", "callback_query"],
                "drop_pending_updates": True,
            },
        )

        if r.get("ok"):
            self.stdout.write(self.style.SUCCESS(
                f"Webhook set successfully:\n  {webhook_url}"
            ))
        else:
            raise CommandError(f"Failed: {r.get('description')}")



    def _request(self, url: str, params: dict = None) -> dict:
        try:
            r = httpx.get(url, params=params, timeout=10)
            return r.json()
        except httpx.TimeoutException:
            raise CommandError("Request timed out.")
        except Exception as e:
            raise CommandError(f"Request failed: {e}")