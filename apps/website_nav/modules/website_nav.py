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
    user_profile = UserProfile.objects.get(user_id=request.user.id)
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
    user_profile = UserProfile.objects.get(user_id=request.user.id)
    #user = User.objects.get(username=request.user.username)
    """
    if user.has_perm('change_user_profile', user_profile):
        print("[+]user has permission")
    """
    if request.method == 'POST':
        # 表单匹配POST中相应的数据，多余的不匹配
        user_profile_form = UserProfileForm(request.POST)
        if user_profile_form.is_valid():
            user_profile_data = user_profile_form.cleaned_data
            user_profile.nickname = user_profile_data['nickname']
            user_profile.phone_1 = user_profile_data['phone_1']
            user_profile.phone_2 = user_profile_data['phone_2']
            user_profile.qq = user_profile_data['qq']
            user_profile.wechat = user_profile_data['wechat']
            user_profile.save()
            return JsonResponse(CODE_MSG['success'])
        else:
            return JsonResponse(CODE_MSG['profile_set_failed'])
    else: 
        return JsonResponse(CODE_MSG['profile_set_failed'])

