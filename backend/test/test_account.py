# -*- coding:utf-8 -*-

from django.test import TestCase, Client
from forms import account_forms
from django.middleware.csrf import get_token, rotate_token
class RegistrationFormTEstCase(TestCase):
    cookies = '';

    def setUp(self):
        self.get_csrf_token()
        #self.registration()
        #self.login()

    def set_user_profile(self):
        account_data = {
            'username': 'ori71e1',
            'nickname': 'ori71e1',
            'phone_1':  '1234567890'
        }   
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/set_user_profile', account_data)
        self.assertEqual(response.status_code, 200)      
        self.assertContains(response, 'status')       

    def tearDown(self):
        print('Account Test End')
    

    def registration(self):
        register_data = {'username': 'ori71e1', 'password': 'ori71e1', 'password2': 'ori71e1'}
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/register', register_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status')
        self.assertTrue('success' in response.content)

    def login(self):
        login_data = {'username': 'ori71e1', 'password': 'ori71e1'}
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/login', login_data)        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status')
        self.assertTrue('success' in response.content)

    #def logout(self):
        
    def get_csrf_token(self):
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.get('/account/get_csrf_token')    
        self.cookies = response.COOKIES
        print(self.cookies)


