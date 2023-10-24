from rest_framework import serializers
from .models import BillingAddress


class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ('id', 'user_id', 'first_name', 'last_name', 'user_mail', 'mobile_no',
        'state','city', 'address', 'pincode', 'order_notes')
