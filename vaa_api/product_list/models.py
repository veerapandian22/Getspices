from django.db import models
from product.models import Product

class ProductList(models.Model):
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   name = models.CharField(max_length=50)
   image_path = models.CharField(max_length=50)
   price = models.IntegerField(max_length=50)
   stack_quantity = models.CharField(max_length=50)
   grade = models.CharField(max_length=50)
   content = models.CharField(null=True)
   manufacturer_from  = models.CharField(max_length=50)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.name