from django.db import models


class User(models.Model):
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=30, unique=True)
   mobile_no = models.IntegerField(unique=True)
   password = models.CharField(max_length=30)
   is_admin = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   mobile_otp = models.IntegerField(null=True, blank=True)
   mobile_otp_generate_timestamp = models.DateTimeField(null=True, blank=True)
   email_otp = models.IntegerField(null=True, blank=True)
   email_otp_generate_timestamp = models.DateTimeField(null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name
   
   class Meta:
        db_table = 'users'
