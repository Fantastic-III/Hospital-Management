from django.db import models
from datetime import date


# Create your models here.
class Appointment(models.Model):
    patient_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    problem_organ = models.CharField(max_length=10)
    problem_description = models.TextField()
    time_batch = models.CharField(max_length=7)
    appointment_date = models.DateField()
    user = models.ForeignKey('User.NewUser', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor.Doctor', on_delete=models.CASCADE)