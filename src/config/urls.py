from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from src.apps.bot import webhook
from src.apps.accounts.views import webapp_auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path(settings.WEBHOOK_PATH, webhook.telegram, name="tg_webhook"),
    path('webapp/auth/', webapp_auth, name='webapp_auth'),

    path("", include("src.apps.academy.urls"), name="academy"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)