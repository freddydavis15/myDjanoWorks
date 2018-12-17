from django.db import models

# Create your models here.
class Student(models.Model):
    student = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    mark = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=13)

    def __str__(self):
        return self.student
