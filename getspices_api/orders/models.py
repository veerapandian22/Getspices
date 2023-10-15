from django.db import models
from users.models import User
from products.models import Product
from product_items.models import ProductItem
from billing_address.models import BillingAddress

class Oderdetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_item_id = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    billing_address_id = models.ForeignKey(BillingAddress, null=True, on_delete=models.CASCADE)
    is_order_placed = models.BooleanField(default=True)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user_id
    
    class Meta:
        db_table = 'orders'

