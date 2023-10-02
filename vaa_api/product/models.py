from django.db import models


class Product(models.Model):
   name = models.CharField(max_length=30)
   image_path = models.CharField(max_length=30)
   price = models.CharField(max_length=6)
   stack_quantity = models.CharField(max_length=5)
   manufacturer_from  = models.CharField(max_length=30)
   content = models.CharField(null=True)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.name