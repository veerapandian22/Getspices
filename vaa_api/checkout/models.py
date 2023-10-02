from django.db import models
from user.models import User

class Checkout(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=30)
   phone = models.IntegerField(null=True)
   address = models.CharField(max_length=500)
   state = models.CharField(max_length=30)
   district = models.CharField(max_length=30)
   pincode = models.IntegerField(null=True)
   message = models.CharField(max_length=1000)
   added_on = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   def __str__(self):
       return self.name