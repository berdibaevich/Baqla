import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from src.utils import (
    parse_init_data,
    Role
)
from .services import get_or_create_user


ROLE_REDIRECTS = {
    Role.STUDENT: "/webapp/student/",
    Role.PARENT: "/webapp/parent/",
    Role.MENTOR: "/webapp/mentor/"
}


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

    if not user.is_active:
        return JsonResponse({"error": "blocked"}, status=403)

    # Redirect
    if is_new or not user.is_verified:
        redirect_url = "/webapp/register/"
    else:
        redirect_url = ROLE_REDIRECTS.get(user.role, "/webapp/register/")

    return JsonResponse({"redirect": redirect_url})



def register(request):
    return render(request, 'academy/register.html')