from django.db import models

# Create your models here.
class Student(models.Model):
    crn = models.IntegerField(unique=True)
    level = models.IntegerField()
    section = models.CharField(max_length=1)
    fullname = models.CharField(max_length=128)

    def __repr__(self):
        return self.fullname

    __str__ = __repr__


class StudentInfo(models.Model):
    address = models.TextField()
    dob = models.DateField(verbose_name="Date Of Birth")

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        verbose_name="student"
    )

    @property
    def crn(self):
        # student_info.crn
        return self.student.crn
