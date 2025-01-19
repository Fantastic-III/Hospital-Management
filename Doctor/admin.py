from django.contrib import admin
from Doctor.models import Doctor


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'qualification', 'speciality', 'experience', 'mobile', 'email', 'password')


admin.site.register(Doctor, DoctorAdmin)
