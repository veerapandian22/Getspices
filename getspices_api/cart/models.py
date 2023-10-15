from django.db import models
from users.models import User
from products.models import Product
from product_items.models import ProductItem


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    product_item_id = models.ForeignKey(ProductItem, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'cart'
