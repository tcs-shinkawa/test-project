from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from .models import AppUser


class LoginTest(APITestCase):
    """
    ログインテスト
    """

    url = "/api/auth/jwt/create/"

    def setUp(self) -> None:
        self.user = AppUser.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

        # パスワードをpasswordに
        users = AppUser.objects.all()
        for user in users:
            user.set_password("password")
            user.save()

    def test_post(self):
        payload = {"username": self.user.username, "password": "wrongpassword"}
        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 401)

        payload = {"username": self.user.username, "password": "password"}

        response = self.client.post(self.url, payload)
        self.assertEqual(response.status_code, 200)
