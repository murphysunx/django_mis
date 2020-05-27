from .models import Customer
from rest_framework import generics
from django.shortcuts import render
from .serializers import CustomerSerializer


#
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


