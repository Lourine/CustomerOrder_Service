import json
from django.contrib.auth import get_user_model as user_model
User = user_model()
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import  OrderSerializer
from .models import Order
from rest_framework.response import Response

class OrderTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email = "customer@savinfo.app",
                                            username = "Customer",
                                            phone_number = "+254722122122",
                                            password = "customer123")
        
        self.token = self.user.tokens()['access']
        self.api_authentication()
        self.order = Order.objects.create(item = "pens", amount=5, customer=self.user)

    def tearDown(self):
        User.objects.all().delete()
        Order.objects.all().delete()        

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer "+ self.token)
    
    def test_post_order(self):
        data = {"item": "books",                               
                "amount": 50}
        response = self.client.post(reverse("order-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(response.data["item"], "books")
        # self.assertEqual(response.data["amount"], 50)
        
    def test_get_customer_orders_by_owner(self):        
        this_customer_id = self.user.id
        response = self.client.get(reverse("order-detail", kwargs={"pk": this_customer_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_single_order_by_owner(self):        
        this_order_id = self.order.id
        response = self.client.get(reverse("order-detail", kwargs={"pk": this_order_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["item"], "pens")
        
    def test_update_single_order_by_owner(self):
        this_order_id = self.order.id
        response = self.client.put(reverse("order-detail", kwargs={"pk": this_order_id}),
                                    )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["amount"], 10)
        
        
    def test_delete_single_order(self):
        this_order_id = self.order.id
        # import pdb; pdb.set_trace()
        response = self.client.delete(reverse("order-detail", kwargs={"pk": this_order_id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 

