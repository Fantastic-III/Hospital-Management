from django.shortcuts import render, redirect
from .models import Doctor
from Appointment.models import Appointment
from datetime import date


# Create your views here.
def load_doctor_homepage(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        return redirect('HomePage')
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, 'homepagedoc.html', {'doctor': doctor})


def load_appointment_list(request):
    doctor_id = request.session.get('doctor_id')
    return render(request, "appointmentlist.html", {'app_data': Appointment.objects.filter(doctor_id=doctor_id, appointment_date=date.today()).order_by('id')})


def load_doctor_settings(request):
    doctor_id = request.session.get('doctor_id')
    return render(request, "doctor_settings.html", {'doctor': Doctor.objects.get(id=doctor_id)})
