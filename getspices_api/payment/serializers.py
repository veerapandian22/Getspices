from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user_id', 'is_payment_success', 'is_upi', 'upi_amount_payed', 'is_cash_on_delivery',
        'cash_amount_payed', 'is_verified_by_admin', 'payment_verified_admin_name', 'payment_verified_date','order_id')
