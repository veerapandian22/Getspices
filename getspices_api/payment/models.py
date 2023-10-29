from django.db import models
from users.models import User

class Payment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_payment_success = models.BooleanField(null=True)
    is_upi = models.BooleanField(null=True)
    upi_amount_payed = models.IntegerField(null=True)
    is_cash_on_delivery= models.BooleanField(null=True)
    cash_amount_payed = models.IntegerField(null=True)
    is_verified_by_admin = models.BooleanField(null=True)
    payment_verified_admin_name = models.CharField()
    payment_verified_date = models.DateTimeField(null=True)
    order_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.is_payment_success
   
    class Meta:
        db_table = 'payment'
