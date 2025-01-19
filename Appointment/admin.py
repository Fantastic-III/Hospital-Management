from django.contrib import admin
from Appointment.models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'gender', 'dob', 'problem_organ', 'problem_description', 'time_batch', 'appointment_date', 'user_id', 'doctor_id')


admin.site.register(Appointment, AppointmentAdmin)