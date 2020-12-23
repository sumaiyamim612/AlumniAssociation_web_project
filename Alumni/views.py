from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from.models import Profile,JobCircular,EventPost

# Create your views here.


def home(request):
    AllEventView=EventPost.objects.filter()[:3]
    AllJobPostView=JobCircular.objects.filter()[:3]
    context={
        'AllJobPostView':AllJobPostView, 
        'AllEventView':AllEventView, 
    }
    return render(request, 'index.html',context)


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
    if request.method=='POST':
        name=request.POST["name"]
        address=request.POST["address"]
        batch=request.POST=["batch"]
        passing_year=request.POST["passing_year"]
        job=request.POST["job"]
        company=request.POST["company"]
        image=request.POST["img"]
        post_create=Profile(
            name=name,
            address=address,
            batch=batch,
            passingYear=passing_year,
            job=job,
            company=company,
            profileImage=image,

        )
        post_create.save()
        print("svae data")
    return render(request, 'edit_profile.html')


def job_post(request):
    if request.method== 'POST':
        jobtitle=request.POST["job_title"]
        companyurl=request.POST["company_url"]
        jobposition=request.POST["job_position"]
        jobnuture=request.POST["job_nature"]
        expreiance=request.POST["experience"]
        workplace=request.POST["workplace"]
        educationalrequierments=request.POST["Educational_Requirement"]
        requierskills=request.POST["Required_Skill"]
        email=request.POST["email"]
        image=request.FILES['image']
        dedline=request.POST["dedline"]
        create_jobpost=JobCircular(
            jobTitle=jobtitle,
            jobDescription=companyurl,
            jobNuture=jobnuture,
            jobPostion=jobposition,
            jobExperiance=expreiance,
            workPlace=workplace,
            educationalRequierments=educationalrequierments,
            mustRequierdSkills=requierskills,
            email=email,
            jobImageBanner=image,
            deadline=dedline
            
        )
        create_jobpost.save()
        print("save post")
        messages.success(
                request, "The Account has been successfully added")
    return render(request, 'job_post.html')


def event_post(request):
    if request.method == 'POST':

        eventtile=request.POST["event_title"]
        eventlink=request.POST["event_link"]
        eventdescription=request.POST["event_discription"]
        eventpalce=request.POST["event_place"]
        eventdate=request.POST["event_date"]
        eventguest=request.POST["event_guest"]
        eventkeynote=request.POST["event_keynote"]
        eventtime=request.POST["event_time"]
        image=request.FILES["image"]
        

        create_event=EventPost(
            eventTitle=eventtile,
            eventLink=eventlink,
            eventDescription=eventdescription,
            eventChifeGuest=eventguest,
            eventKeyNote=eventkeynote,
            eventlocation=eventpalce,
            eventStartTime=eventtime,
            eventDate=eventdate,
            eventImage=image
        )
        create_event.save()
        print("save event")
        messages.success(
                request, "The Account has been successfully added")
    return render(request, 'event_post.html')


def job_view(request):
    AllJobPostView=JobCircular.objects.all()
    # print(AllJobPostView.0.jobImageBanner)
    context={
      'AllJobPostView':AllJobPostView,  
    }
    return render(request, 'job_view.html',context)


def event_view(request):
    AllEventView=EventPost.objects.all()
    context={
      'AllEventView':AllEventView,  
    }
    return render(request, 'event_view.html',context)
