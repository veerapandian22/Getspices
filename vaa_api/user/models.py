from django.db import models


class User(models.Model):
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=30)
   ph_no = models.CharField(max_length=20)
   password = models.CharField(max_length=30)
   is_admin = models.BooleanField(default=False)
   added_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.name