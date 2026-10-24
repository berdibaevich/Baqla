from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def webapp_auth(request):
    print(request.method)
    print(request.body)

    return JsonResponse({"success": 200})