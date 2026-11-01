import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from src.utils import (
    parse_init_data
)
from .services import get_or_create_user



@csrf_exempt
def webapp_auth(request):

    if request.method != "POST":
        return JsonResponse({"error": "Failed: Method not allowed."}, status=405)

    try:
        body = json.loads(request.body)
        init_data = body.get("initData", "")
    except Exception:
        return JsonResponse({"error": "Failed: Invalid body."}, status=400)
 
    tg_user = parse_init_data(init_data)
    
    if not tg_user:
        return JsonResponse(
            {"error": "Failed: Authorization problem. Please open again the WebApp."}
        )

    user, is_new = get_or_create_user(tg_user)

    print("user: ", user)
    print("is_new: ", is_new)


    return JsonResponse({"success": 200})