from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    qualification = models.CharField(max_length=30)
    speciality = models.CharField(max_length=20)
    experience = models.IntegerField()
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=8)
