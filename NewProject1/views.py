from django.shortcuts import render, redirect
from User.models import NewUser as User
from Doctor.models import Doctor


def load_login_page(request):

    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Get username and password.
        role = request.POST.get('role')

        if role == "user":
            try:
                user = User.objects.get(username=username, password=password)  # Check whether the user exists.
                request.session['role'] = "user"
                request.session['user_id'] = user.id
                return redirect(f'/my-homepage')
            except User.DoesNotExist:  # If user doesn't exists.
                error_message = "Invalid username or password"
        elif role == "doctor":
            try:
                doctor = Doctor.objects.get(name=username, password=password)  # Check whether the user exists.
                request.session['role'] = "doctor"
                request.session['doctor_id'] = doctor.id
                return redirect(f'/doc-homepage')
            except Doctor.DoesNotExist:  # If doctor doesn't exist.
                error_message = "Invalid username or password"
        else:
            print("Invalid role")
    return render(request, 'login.html', {'error_message': error_message})


def logout_view(request):
    request.session.flush()
    return redirect('/')


def load_homepage(request):
    if request.session.get('role') == "user":
        return redirect('/my-homepage')
    elif request.session.get('role') == "doctor":
        return redirect('/doc-homepage')
    return render(request, "homepage.html")  # Otherwise go to general home page.


def load_about(request):
    return render(request, "about.html")


def load_create_account(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=name, password=password)
        user.save()
        return redirect(f"/my-homepage?name={name}")
    return render(request, "createaccount.html")
