from django.shortcuts import render ,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def home (request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["password_confirm"]
        if password == confirm_password:
            user_Create=User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user_Create.save()
            print("account create")
            messages.success(request, "The Account has been successfully added")
            return redirect('registration')
        else:
            messages.error(request, "password not same")
            print("password not same")
            return redirect('registration')
    else:        
        return render(request,'registration.html')
def profile (request):
    return render(request,'profile.html')

def job_view (request):
    return render(request,'job_view.html')    