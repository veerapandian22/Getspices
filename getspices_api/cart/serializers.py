from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'product_id', 'product_item_id')
