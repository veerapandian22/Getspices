from django.db import models
from products.models import Product

class ProductItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=5, unique=True)
    item_name = models.CharField(max_length=10)
    item_grade = models.CharField(max_length=10, unique=True)
    item_img_path = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=5000)
    item_price = models.IntegerField()
    stack_qty = models.IntegerField()
    available_qty = models.IntegerField()
    manufacturer_from  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name
    
    class Meta:
        db_table = 'product_items'