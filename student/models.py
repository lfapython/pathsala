from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=128)
    address = models.TextField()
    dob = models.DateField(verbose_name="Date Of Birth")

    def __repr__(self):
        return self.fullname

    __str__ = __repr__
