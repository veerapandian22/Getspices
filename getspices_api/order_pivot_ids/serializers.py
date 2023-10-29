from rest_framework import serializers
from .models import OrderPivotIds


class OrderPivotIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPivotIds
        fields = ('user_id', 'order_id', 'billing_id', 'payment_id', 'order_tracking_id')
