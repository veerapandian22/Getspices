from django.db import models

class Users(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=20)
   email = models.CharField(max_length=20)
   ph_no = models.IntegerField()
   password = models.CharField(max_length=20)
   added_on = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.name, self.email, self.ph_no, self.added_on