from rest_framework import serializers
from .models import OrderTracking


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = ('user_id', 'order_placed', 'order_processed', 'order_ready_to_ship',
                  'order_shipped', 'shipping_details', 'order_delivered')
