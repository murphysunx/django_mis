from .models import Order
from rest_framework import generics
from django.shortcuts import render
from .serializers import OrderSerializer


# Create your views here.
class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
