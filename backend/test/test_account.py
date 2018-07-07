# -*- coding:utf-8 -*-

from django.test import TestCase, Client
from forms import account_forms
from django.middleware.csrf import get_token, rotate_token
from http import cookies
from pprint import pprint
import json
class RegistrationFormTEstCase(TestCase):
    def __init__(self, arg):    
        super(RegistrationFormTEstCase, self).__init__(arg)
        self.cookies = cookies.SimpleCookie()
        self.csrf_token = ''
        self.client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
    def setUp(self):
        print("-"*70)
        print("[+]Account Test Begin")
        print("\n[+]Set Up")        
        self.get_csrf_token()
        self.registration()
        self.login()

    def tearDown(self):
        print("\n[+]Tear Down")
        print("[+]Test End")
        print("-"*70)

   
    def test_csrf(self):
        print("\n[+]Test CSRF begin:")
        print("[+]CSRF Token: %s" % self.csrf_token)
    def test_user_profile(self):
        self.set_user_profile()
        self.get_user_profile()


    # 此处要么自己设置request要么使用client内置的登录方式
    def set_user_profile(self):
        account_data = {
            'nickname': 'ori71e1',
            'phone_1':  '1234567890',
            'phone_2': '12',
            'qq': '12',
            'wechat': '12'
        }   
        account_data['X-CSRFToken'] = self.csrf_token
        response = self.client.post('/account/set_user_profile', account_data)
        json_data = self.value_to_json(response.getvalue())
        self.assertEqual(response.status_code, 200)
        print("[+]Set User Profile: %s" % json_data)    

    def get_user_profile(self):
        account_data = {
            'nickname': 'ori71e1',
            'phone_1':  '1234567890',
            'phone_2': '12',
            'qq': '12',
            'wechat': '12'
        }   
        account_data['X-CSRFToken'] = self.csrf_token
        response = self.client.post('/account/get_user_profile', account_data)
        json_data = self.value_to_json(response.getvalue())
        self.assertEqual(response.status_code, 200)
        print("[+]Get User Profile: %s" % json_data)   

    def registration(self):
        register_data = {'username': 'ori71e1', 'password': 'ori71e1', 'password2': 'ori71e1'}
        register_data['X-CSRFToken'] = self.csrf_token
        response = self.client.post('/account/register', register_data)
        json_data = self.value_to_json(response.getvalue())
        self.assertEqual(response.status_code, 200)
        print("[+]Registration Response: %s" % json_data)

    def login(self):
        #self.client.login(username='ori71e1', password='ori71e1')
        
        login_data = {'username': 'ori71e1', 'password': 'ori71e1'}
        login_data['X-CSRFToken'] = self.csrf_token
        response = self.client.post('/account/login', login_data)        
        json_data = self.value_to_json(response.getvalue())
        self.assertEqual(response.status_code, 200)
        print("[+]Login Response: %s" % json_data)

    #def logout(self):
        
    def get_csrf_token(self):
        response = self.client.get('/account/get_csrf_token') 
        self.cookies = response.cookies
        self.csrf_token = self.parse_cookie(str(self.cookies['csrftoken']))['csrftoken']
        


    def parse_cookie(self, cookie):
        """
        Return a dictionary parsed from a `Cookie:` header string.
        """
        cookiedict = {}
        cookie = cookie.strip('Set-Cookie:')
        for chunk in cookie.split(';'):
            if '=' in chunk:
                key, val = chunk.split('=', 1)
            else:
                # Assume an empty name per
                # https://bugzilla.mozilsla.org/show_bug.cgi?id=169091
                key, val = '', chunk
            key, val = key.strip(), val.strip()
            if key or val:
                # unquote using Python's algorithm.
                cookiedict[key] = cookies._unquote(val)
        return cookiedict

    def value_to_json(self, value):
        value_to_str = value.decode('utf-8')
        value_to_json = json.loads(value_to_str)   
        return value_to_json    
