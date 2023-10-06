from django.db import models


class ContactUS(models.Model):
   name = models.CharField(max_length=30)
   email = models.CharField(null=True, max_length=30)
   phone = models.CharField(max_length=10)
   subject = models.CharField(null=True, max_length=30)
   message = models.CharField(max_length=1000)
   added_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.name