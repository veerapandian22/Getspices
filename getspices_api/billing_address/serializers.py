from rest_framework import serializers
from .models import BillingAddress


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ('id', 'user_id', 'user_name', 'user_mail', 'mobile_no', 'address',
                  'state', 'district', 'city', 'pincode', 'order_notes')
