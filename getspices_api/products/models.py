from django.db import models


class Product(models.Model):
    hsn_code = models.CharField(max_length=5, unique=True)
    product_code = models.CharField(max_length=4, unique=True)
    product_name = models.CharField(max_length=30)
    product_img_path = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField()
    stack_qty = models.IntegerField()
    available_qty = models.IntegerField()
    manufacturer_from  = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.product_name
    
    class Meta:
        db_table = 'products'
