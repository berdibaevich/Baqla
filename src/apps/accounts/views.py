import re
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from src.utils import (
    parse_init_data,
    Role
)
from .services import get_or_create_user
from .forms import StudentRegisterForm

from src.integrations import github_service, GitHubError



ROLE_REDIRECTS = {
    Role.STUDENT: "/webapp/student/",
    Role.PARENT: "/webapp/parent/",
    Role.MENTOR: "/webapp/mentor/"
}

GH_USERNAME_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


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
    print("redirect_url: ", redirect_url)
    return JsonResponse({"redirect": redirect_url})



def register(request):
    form = StudentRegisterForm()
    return render(request, 'academy/register.html', {'form': form})



async def check_github(request):
    username = request.GET.get("username", "").strip()

    if not GH_USERNAME_RE.match(username):
        return JsonResponse({"exists": False, "error": "invalid"})

    try:
        exists = await github_service.check_user_exists(username)
    except GitHubError:
        return JsonResponse({"exists": False, "error": "unavailable"}, status=502)

    return JsonResponse({'exists': exists})