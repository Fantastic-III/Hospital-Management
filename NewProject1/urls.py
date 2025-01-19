"""
URL configuration for NewProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from NewProject1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.load_homepage, name="HomePage"),
    path("my-homepage/", include('User.urls'), name="HomePageLogged"),
    path("doc-homepage/", include('Doctor.urls'), name="HomePageDoc"),
    path("about-us", views.load_about, name="AboutUs"),
    path("login", views.load_login_page, name="Login"),
    path('logout', views.logout_view, name='Logout'),
    path("create-account", views.load_create_account, name="CreateAccount"),
]
