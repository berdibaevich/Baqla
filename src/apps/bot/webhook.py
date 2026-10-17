import json
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt
from aiogram import types

from .loader import bot, dp


async def handle_webhook(req: HttpRequest):
    if req.method != 'POST':
        return HttpResponse("Method Not Allowed", status=405)

    url = req.build_absolute_uri()
    index = url.rfind("/")
    token = url[index+1:]

    if token == settings.BOT_TOKEN:
        raw_data = req.body
        json_string = raw_data.decode('utf-8')
        update_data = json.loads(json_string)
        update = types.Update(**update_data)
        await dp.feed_update(bot=bot, update=update)

        return HttpResponse("OK", status=200)
    else:
        return HttpResponse("ERROR", status=403)


@csrf_exempt
def telegram(request: HttpRequest):
    try:
        response = async_to_sync(handle_webhook)(req=request)
        return response
    except Exception as e:
        return HttpResponse("OK", status=200)


# SetWebhook
# https://api.telegram.org/bot<TOKEN>/setWebhook?url=<DOMEN>/webhook/<TOKEN>

# GetWebhookInfo
# https://api.telegram.org/bot<TOKEN>/getWebhookInfo

# DeleteWebhook
# https://api.telegram.org/bot<TOKEN>/deleteWebhook