from django.db import models
from users.models import User

class BillingAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    user_mail = models.CharField(max_length=30)
    mobile_no = models.IntegerField(null=True)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField(null=True)
    order_notes = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'billing_address'
