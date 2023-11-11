from .models import Cart
from rest_framework import serializers
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from product_items.serializers import ProductItemSerializer


class CartSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user_id', read_only=True)
    product_details = ProductSerializer(source='product_id', read_only=True)
    product_item_details = ProductItemSerializer(source='product_item_id', read_only=True)
    
    class Meta:
        model = Cart
        fields = ('id', 'user_id', 'product_id', 'product_item_id', 'user_details', 'product_details',
                  'product_item_details')

        # fields = "__all__"
