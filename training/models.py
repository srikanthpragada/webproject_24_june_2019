from django.db import models


# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null=True)
    course = models.CharField(max_length=10)
    feepaid = models.IntegerField()

    def __str__(self):
        return self.fullname + "," + self.course
