from rest_framework import serializers
from .models import Oderdetails


class OderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oderdetails
        fields = ('id', 'user_id', 'product_id', 'product_item_id', 'billing_address_id', 'is_order_placed', 'is_delivered')
