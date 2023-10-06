from django.db import models


class Subscribe(models.Model):
   email = models.CharField(max_length=30)
   added_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.email