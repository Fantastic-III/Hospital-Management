from django.shortcuts import render, redirect
from .models import NewUser as User
from Appointment.models import Appointment
from Doctor.models import Doctor
from datetime import date


# Create your views here.
def load_logged_homepage(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('HomePage')
    user = User.objects.get(id=user_id)
    return render(request, 'homepagelogged.html', {'user': user})


def load_appointment_form(request):
    if request.method == 'POST':
        name = request.POST.get('patient-name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        problem_organ = request.POST.get('problem-organ')
        problem_description = request.POST.get('problem-description')
        session_batch = request.POST.get('session-batch')
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        if problem_organ == "General":
            doctor = Doctor.objects.get(speciality="General")
        elif problem_organ == "Bones":
            doctor = Doctor.objects.get(speciality="Bones")
        elif problem_organ == "ENT":
            doctor = Doctor.objects.get(speciality="ENT")
        elif problem_organ == "Mouth":
            doctor = Doctor.objects.get(speciality="Mouth")
        elif problem_organ == "Throat":
            doctor = Doctor.objects.get(speciality="Throat")
        elif problem_organ == "Heart":
            doctor = Doctor.objects.get(speciality="Heart")
        elif problem_organ == "Lungs":
            doctor = Doctor.objects.get(speciality="Lungs")
        elif problem_organ == "Kidneys":
            doctor = Doctor.objects.get(speciality="Kidneys")
        elif problem_organ == "Other":
            doctor = Doctor.objects.get(speciality="Other")
        app = Appointment(patient_name=name, gender=gender, dob=dob, problem_organ=problem_organ, problem_description=problem_description, time_batch=session_batch, appointment_date=date.today(), user=user, doctor=doctor)
        app.save()
        return redirect('/')
    return render(request, 'appointment.html')


def load_profile(request):
    user = User.objects.get(id=request.session.get('user_id'))
    return render(request, "userprofile.html", {'user': user})


def load_appointment_history(request):
    user_id = request.session.get('user_id')
    return render(request, "appointmenthistory.html", {'app_data': Appointment.objects.filter(user_id=user_id).order_by('-id')})


def load_change_password(request):
    if request.method == "POST":
        new_password = request.POST.get('new-password')
        confirm_password = request.POST.get('confirm-password')
        user_id = request.session.get('user_id')
        user = User.objects.get(id=user_id)
        if new_password == user.password:
            return render(request, "passwordchange.html", {'error_message': "New password cannot be same as old password"})
        elif new_password == confirm_password:
            user.password = new_password
            user.save()
            return redirect('/my-homepage/profile')
        else:
            return render(request, "passwordchange.html", {'error_message': "Passwords don't match"})
    return render(request, "passwordchange.html")