from django.db import models
from users.models import User


class OrderTracking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_placed = models.BooleanField(null=True)
    order_processed = models.BooleanField(null=True)
    order_ready_to_ship = models.BooleanField(null=True)
    order_shipped = models.BooleanField(null=True)
    shipping_details = models.CharField(null=True)
    order_delivered = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'order_tracking'
