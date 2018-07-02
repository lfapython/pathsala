from django.db import models

# Create your models here.
class Teacher(models.Model):
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    phone_number = models.CharField(max_length=16)
