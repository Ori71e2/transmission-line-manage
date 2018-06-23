# -*- coding:utf-8 -*-

from django.test import TestCase, Client
from . forms import RegistrationForm

class RegistrationFormTEstCase(TestCase):
    
    def test_registration(self):
        register_data = {'username': 'ori71e2', 'password': 'ori71e2', 'password2': 'ori71e2'}
        client = Client(enforce_csef_checks=False, HTTP_USER_AGENT='Mozilla/5.0')
        response = client.post('/account/register', register_data)
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'OK')
        #self.assertTrue('OK' in response.content)
