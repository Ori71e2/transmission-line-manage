# -*- coding:utf-8 -*-

from django.test import TestCase, Client
from forms import account_forms

class RegistrationFormTEstCase(TestCase):
    def setUp(self):
        print('Account Test Begin')



    def test_registration(self):
        register_data = {'username': 'ori71e1', 'password': 'ori71e1', 'password2': 'ori71e1'}
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/register', register_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'status')
        #self.assertTrue('OK' in response.content)
        account_data = {
            'user_profile_form' : [
                'username': 'ori71e1',
                'nickname': 'ori71e1'
                
            ],
            'user': [
                'phone_1':  '1234567890'
            ]
        }   
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/set_user_profile', account_data)
        self.assertEqual(response.status_code, 200)      
        self.assertContains(response, 'status') 
    """  
    def test_set_user_profile(self):
        account_data = {
            'username': 'ori71e1',
            'nickname': 'ori71e1',
            'phone_1':  '1234567890'
        }   
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/set_user_profile', account_data)
        self.assertEqual(response.status_code, 200)      
        self.assertContains(response, 'status')       
    """
    def tearDown(self):
        print('Account Test End')