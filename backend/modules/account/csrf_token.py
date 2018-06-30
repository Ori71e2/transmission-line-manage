from django.http import JsonResponse

from modules.RESPONSE import CODE_MSG
from django.middleware.csrf import get_token


def get_csrf_token(request):
    response = {}
    try:
        if request.method == 'GET':
            get_token(request)
        response = CODE_MSG['success']
    except Exception as e:
        response = CODE_MSG['token_get_failed']
    return JsonResponse(response)
