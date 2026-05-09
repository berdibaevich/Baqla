from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import Bot
from asyncio import run


ALLOWED_UPDATES = ["message", "callback_query"]


class Command(BaseCommand):
    help = 'Sets the Telegram Webhook URL.'

    def handle(self, *args, **options):
        run(self._set_webhook())
    
    async def _set_webhook(self):
        bot = Bot(token=settings.BOT_TOKEN)

        try:
            success = await bot.set_webhook(
                url=settings.WEBHOOK_URL,
                allowed_updates=ALLOWED_UPDATES,
                drop_pending_updates=True
            )
            if success:
                self.stdout.write(self.style.SUCCESS('✅ Webhook successfully set!'))

                info = await bot.get_webhook_info()
                self.stdout.write(f"Current allowed updates: {info.allowed_updates}")
            
            else:
                self.stdout.write(self.style.ERROR('❌ Failed to set webhook.'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Unexpected error during webhook setup: {e}"))

        finally:
            await bot.session.close()