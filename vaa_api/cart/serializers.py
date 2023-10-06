from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'product_list', 'product_name', 'product_path', 'price', 'quantity', 'total')
