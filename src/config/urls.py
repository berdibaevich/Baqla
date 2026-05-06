from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.bot import webhook


urlpatterns = [
    path('admin/', admin.site.urls),
    path(settings.WEBHOOK_PATH, webhook.telegram, name="tg_webhook"),
]
