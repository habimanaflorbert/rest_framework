from rest_framework.test import APITestCase,APIClient
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self):
        account_url='/user/'
        self.users_url=account_url
        self.login_url ='/login/'
        self.user_data = {
    "username":"rich",
    "first_name": "Richard",
    "last_name": "Richman",
    "email":"habimanaflorbert@gmail.com",
    "password":"Rwanda2025",
    "re_password": "Rwanda2025"
}
        self.login_with_phone_data = {
            "username" : "+250788888888",
            "password": "{YY[v9q{,8_UrP(+",
        }
        
        
        return super().setUp()

    def tearDown(self):
        return super().tearDown()