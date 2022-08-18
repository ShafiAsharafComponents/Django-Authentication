from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    employee = models.BooleanField(default=False)
    team_lead = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

# class Customers(models.Model):
#     customer_id = models.AutoField(primary_key=True)
#     customer_username = models.CharField(max_length=200, null=False, unique=True)
#     customer_name = models.CharField(max_length=10, null=False)
#     customer_email = models.CharField(max_length=80, null=False)
#     customer_password = models.CharField(max_length=10, null=False)
#     customer_image = models.ImageField(upload_to='images', null=False)
#
#     def __str__(self):
#         return self.customer_name
#
#     def save(self, *args, **kwargs):
#         self.crew_password = make_password(self.customer_password)
#         super(Customers, self).save(*args, **kwargs)
