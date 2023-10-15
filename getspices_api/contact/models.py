from django.db import models


class Contact(models.Model):
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=30)
   message = models.CharField(max_length=1000)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.name
   
   class Meta:
        db_table = 'contact'
