from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'name', 'email', 'phone', 'address', 'state', 'district', 'pincode','message')
