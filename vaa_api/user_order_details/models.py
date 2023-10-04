from django.db import models
from user.models import User
from product.models import Product
from product_list.models import ProductList


class Oderdetails(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
   product_list = models.ForeignKey(ProductList, null=True, on_delete=models.CASCADE)
   product_name = models.CharField(max_length=30)
   product_path = models.CharField(max_length=30)
   price = models.IntegerField()
   quantity = models.IntegerField()
   total = models.IntegerField()
   added_on = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.name
