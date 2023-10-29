from django.db import models
from users.models import User
from orders.models import Oderdetails
from billing_address.models import BillingAddress
from payment.models import Payment
from order_tracking.models import OrderTracking


class OrderPivotIds(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Oderdetails, on_delete=models.CASCADE)
    billing_id = models.ForeignKey(BillingAddress, on_delete=models.CASCADE, null=True)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    order_tracking_id = models.ForeignKey(OrderTracking, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id
   
    class Meta:
        db_table = 'order_pivot_ids'
