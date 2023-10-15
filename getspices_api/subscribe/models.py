from django.db import models


class Subscribe(models.Model):
   email = models.CharField(max_length=30)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.email
   
   class Meta:
        db_table = 'subscribe'