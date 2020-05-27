from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'order_no', 'order_status', 'product_count', 'product_amount_total', 'order_date')
