from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    user_name= models.CharField(max_length=61)
    job =models.CharField(max_length=200)

    def __str__(self):
        return self.user_name+'-'+self.job
