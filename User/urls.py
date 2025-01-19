from django.urls import path
from User import views

urlpatterns = [
    path('', views.load_logged_homepage, name="UserHomePage"),
    path('appointment', views.load_appointment_form, name="AppointmentForm"),
    path('profile', views.load_profile, name="Profile"),
    path('appointment-history', views.load_appointment_history, name="AppointmentHistory"),
    path('change-password', views.load_change_password, name="ChangePassword"),
]
