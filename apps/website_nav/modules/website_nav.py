from django.http import JsonResponse, HttpResponse
from website_nav.models import Website
from website_nav.forms import WebsiteForm
from common_modules.RESPONSE import CODE_MSG
#from modules.decorator import auth_check

from django.contrib.auth import get_user_model
User = get_user_model()
#@auth_check
def get_website(request):
    website = Website.objects.get(user_id=request.user.id)
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

    website = Website.objects.get(user_id=request.user.id)
    """
    if user.has_perm('change_user_profile', user_profile):
        print("[+]user has permission")
    """
    if request.method == 'POST':
        # 表单匹配POST中相应的数据，多余的不匹配
        website_form = WebsiteForm(request.POST)
        if website_form.is_valid():
            website_data = website_form.cleaned_data
            website.name = website_data['name']
            website.page_count = website_data['page_count']
            website.save()
            return JsonResponse(CODE_MSG['success'])
        else:
            return JsonResponse(CODE_MSG['website_set_failed'])
    else: 
        return JsonResponse(CODE_MSG['website_set_failed'])
