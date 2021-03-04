from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Order
from . serializers import OrderSerializer
from authentication.models import User

ORDERS_URL = reverse('orders')
class OrderTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email = "customer@savinfo.app",
                                            username = "Customer",
                                            
                                            phone_number = "+254722122122",
                                            password = "customer123")
        

        self.order = Order.objects.create(item = "pens", amount=5, customer=self.user)

    def tearDown(self):
        User.objects.all().delete()
        Order.objects.all().delete()