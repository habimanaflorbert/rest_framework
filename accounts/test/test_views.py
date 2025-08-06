from django.urls import reverse
from accounts.test.test_setup import TestSetup
from django.contrib.auth.models import User


class TestUserViewSet(TestSetup):
    def test_account_creation(self):
        reg_res = self.client.post(
        self.users_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(reg_res.status_code,201)
     