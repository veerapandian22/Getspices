from rest_framework import serializers
from .models import Checkout


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('user', 'name', 'email', 'phone', 'address', 'state', 'district', 'pincode','message')
