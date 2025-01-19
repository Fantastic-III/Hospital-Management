from django.urls import path
from Doctor import views

urlpatterns = [
    path('', views.load_doctor_homepage, name='DocHomePage'),
    path('todays-appointments', views.load_appointment_list, name='TodaysAppointments'),
    path('doctor-settings', views.load_doctor_settings, name='DocSettings'),
]
