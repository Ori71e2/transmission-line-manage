from django.http import JsonResponse, HttpResponse
from models.account_tb import UserProfile
from django.contrib.auth.models import User

from forms.account_forms import UserProfileForm
from modules.RESPONSE import CODE_MSG
from modules.decorator import auth_check

@auth_check()
def get_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    nickname = user_profile.nickname
    phone_1 = user_profile.phone_1
    phone_2 = user_profile.phone_2
    qq = user_profile.qq
    wechat = user_profile.wechat
    data = {'nickname': nickname, 'phone_1': phone_1, 'phone_2': phone_2, 'qq': qq, 'wechat': wechat}
    return JsonResponse(data)
# 这里注意越权漏洞攻击
#@auth_check()
def set_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
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

