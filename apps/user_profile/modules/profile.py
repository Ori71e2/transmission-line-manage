from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import DataError, Error
from django.http import JsonResponse, HttpResponse
from user_profile.models import UserProfile
from user_profile.forms import UserProfileForm
from common_modules.RESPONSE import CODE_MSG
#from modules.decorator import auth_check

from django.contrib.auth import get_user_model
User = get_user_model()
#@auth_check
def get_user_profile(request):
    print (request.user)
    try:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        return JsonResponse(CODE_MSG['object_does_not_exist'])
    except MultipleObjectsReturned:
        return JsonResponse(CODE_MSG['multiple_objects_returned'])
    except Error:
        return JsonResponse(CODE_MSG['database_error'])
    id = user_profile.id
    nickname = user_profile.nickname
    phone_1 = user_profile.phone_1
    phone_2 = user_profile.phone_2
    qq = user_profile.qq
    wechat = user_profile.wechat
    user_id = user_profile.user_id
    data = {'id':id, 'nickname': nickname, 'phone_1': phone_1, 'phone_2': phone_2, 'qq': qq, 'wechat': wechat, 'user_id':user_id}
    CODE_MSG['success']['data'] = data
    return JsonResponse(CODE_MSG['success'])
# 这里注意越权漏洞攻击
#@auth_check()
def set_user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user_id=request.user.id)
    except MultipleObjectsReturned:
        return JsonResponse(CODE_MSG['multiple_objects_returned'])
    except ObjectDoesNotExist:
        return JsonResponse(CODE_MSG['object_does_not_exist'])
    except Error:
        return JsonResponse(CODE_MSG['database_error'])
    #user = User.objects.get(username=request.user.username)
    """
    if user.has_perm('change_user_profile', user_profile):
        print("[+]user has permission")
    """
    if request.method == 'POST':
        # 表单匹配POST中相应的数据，多余的不匹配
        print(request.POST)
        user_profile_form = UserProfileForm(data=request.POST)
        #print(user_profile_form)
        if user_profile_form.is_valid():
            user_profile_data = user_profile_form.cleaned_data
            user_profile.nickname = user_profile_data['nickname']
            user_profile.phone_1 = user_profile_data['phone_1']
            user_profile.phone_2 = user_profile_data['phone_2']
            user_profile.qq = user_profile_data['qq']
            user_profile.wechat = user_profile_data['wechat']
            try:
                user_profile.save()
            except Error:
                return JsonResponse(CODE_MSG['database_error'])
            return JsonResponse(CODE_MSG['success'])
        else:
            return JsonResponse(CODE_MSG['profile_set_failed'])
    else: 
        return JsonResponse(CODE_MSG['profile_set_failed'])

