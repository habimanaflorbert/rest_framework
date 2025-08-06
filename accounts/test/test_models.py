from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            email="test@jamboShop.com",
            first_name="Test1",
            last_name="Test2",
            password="{YY[v9q{,8_UrP(+",
        )
        User.objects.create(
            email="test2@jamboShop.com",
            first_name="Test21",
            last_name="Test22",
            password="{YY[v9q{,8_UrP(+",
        )