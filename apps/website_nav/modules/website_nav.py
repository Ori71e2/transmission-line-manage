from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import OperationalError, DataError, Error
from django.http import JsonResponse, HttpResponse
from website_nav.models import Website
from website_nav.forms import WebsiteForm
from common_modules.RESPONSE import CODE_MSG
import json
#from modules.decorator import auth_check

#@auth_check
def get_website(request):
    print("Get Website")
    try:
        website = Website.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        return JsonResponse(CODE_MSG['object_does_not_exist'])
    except MultipleObjectsReturned:
        return JsonResponse(CODE_MSG['multiple_objects_returned'])
    except Error:
        return JsonResponse(CODE_MSG['database_error'])
    id = website.id
    name = website.name
    page_count = website.page_count
    user_id  = website.user_id
    data = {'id':id, 'user_id':user_id, 'name':name, 'page_count':page_count}
    CODE_MSG['success']['data'] = data
    return JsonResponse(CODE_MSG['success'])
# 这里注意越权漏洞攻击
#@auth_check()

def set_website(request):
    try:
        website = Website.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        return JsonResponse(CODE_MSG['object_does_not_exist'])
    except MultipleObjectsReturned:
        return JsonResponse(CODE_MSG['multiple_objects_returned'])
    except Error:
        return JsonResponse(CODE_MSG['database_error'])
    """
    if user.has_perm('change_user_profile', user_profile):
        print("[+]user has permission")
    """
    if request.method == 'POST':
        website_form = WebsiteForm(request.POST)
        if website_form.is_valid():
            website_data = website_form.cleaned_data
            website.name = website_data['name']
            website.page_count = website_data['page_count']
            try:
                website.save()
            except Error:
                return JsonResponse(CODE_MSG['database_error'])
            return JsonResponse(CODE_MSG['success'])
        else:
            return JsonResponse(CODE_MSG['website_set_failed'])
    else: 
        return JsonResponse(CODE_MSG['website_set_failed'])
