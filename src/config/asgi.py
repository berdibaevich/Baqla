import os
import django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

application = get_asgi_application()

from apps.bot.loader import dp, setup_routers

setup_routers(dp)
