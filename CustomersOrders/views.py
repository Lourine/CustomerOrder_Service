from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order
from rest_framework import permissions
from .permissions import IsOwner
from .send_sms import SendSMS

# Create your views here.
class OrderListAPIView(ListCreateAPIView):
    serializer_class=OrderSerializer
    queryset = Order.objects.all()
    permission_classes= (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        customer = self.request.user
        order_item = serializer.validated_data['item']
        order_amount = serializer.validated_data['amount']  
        SendSMS(customer.username, customer.phone_number, order_item, order_amount)
        return serializer.save(customer=customer)
        

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)

class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=OrderSerializer
    queryset = Order.objects.all()
    permission_classes= (permissions.IsAuthenticated, IsOwner,)
    lookup_field ="id"

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user)
