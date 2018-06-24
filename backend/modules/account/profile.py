from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models.account_tb import UserProfile
from django.contrib.auth.models import User

from forms.account_forms import UserProfileForm
@login_required(login_url='/account/login')
def get_user_profile(request):
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    return HttpResponse({'user': user, 'user_pfofile': user_profile})
# 这里注意越权漏洞攻击
@login_required(login_url='/account/login')
def set_user_profile(request):
    print(request.POST)
    #user_profile = UserProfile.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    print(user_profile)
    if request.method == 'POST':
        # 表单匹配POST中相应的数据，多余的不匹配
        user_profile_form = UserProfileForm(request.POST)
        if user_profile_form.is_valid():
            user_profile_data = user_profile_form.clean_data
            user_profile.nickname = user_profile_data['nickname']
            user_profile.phone_1 = user_profile_data['phone_1']
            user_profile.phone_2 = user_profile_data['phone_2']
            user_profile.qq = user_profile_data['qq']
            user_profile.wechat = user_profile_data['wechat']
            user_profile.save()
            return HttpResponse(True)
        else:
            return HttpResponse(True)
    else: 
        return HttpResponse(True)
