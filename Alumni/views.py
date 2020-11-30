from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'you are login')
                return redirect('profile')
            else:
                messages.error(request, ' incorret Username Password!')
                return redirect('login')

        else:
            messages.error(request, '  Username & Password are invalid!')
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["password_confirm"]
        if password == confirm_password:
            user_Create = User.objects.create_user(
                username=username,
                first_name=first_name,
                email=email,
                password=password
            )
            user_Create.save()
            print("account create")
            messages.success(
                request, "The Account has been successfully added")
            return redirect('registration')
        else:
            messages.error(request, "password not same")
            print("password not same")
            return redirect('registration')
    else:
        return render(request, 'registration.html')


def profile(request):
    
    return render(request, 'profile.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def job_post(request):
    return render(request, 'job_post.html')


def event_post(request):
    return render(request, 'event_post.html')


def job_view(request):
    return render(request, 'job_view.html')


def event_view(request):
    return render(request, 'event_view.html')
