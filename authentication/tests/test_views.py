from django.urls import reverse


from ..models import User
from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register_correctly(self):
        data = {
            'email': 'test@example.com',
            'username': 'test',
            'password': 'test1234',
            'phone_number': '12345678',
        }
        response= self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code, 201)
   
    def test_registration_missing_field(self):
        data = {"email": "test4@savinfo.app",
                "password": "password456",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, 400)
        

    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(
            self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 401)

    def test_user_can_login_after_verification(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        # import pdb; pdb.set_trace()
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)
        
    