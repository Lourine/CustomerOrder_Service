from authentication.models import User
from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()

        self.user_data = {
            'email': self.fake.email(),
            'username': self.fake.email().split('@')[0],
            'password': self.fake.email(),
            'phone_number': self.fake.phone_number()
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
