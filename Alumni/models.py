from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class JobCircular (models.Model):
    jobTitle = models.CharField(max_length=100)
    jobDescription = models.CharField(max_length=255)
    jobPostion = models.CharField(max_length=100)
    jobNuture = models.CharField(max_length=50)
    jobExperiance = models.CharField(max_length=50)
    workPlace = models.CharField(max_length=120)
    educationalRequierments = models.CharField(max_length=150)
    mustRequierdSkills = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    jobImageBanner = models.ImageField(upload_to='media/')
    deadline = models.CharField(max_length=30)


class EventPost(models.Model):
    eventTitle = models.CharField(max_length=100)
    eventLink=models.CharField(max_length=60,blank=True,null=True)
    eventKeyNote=models.CharField(max_length=255,blank=True,null=True)
    eventImage = models.ImageField(upload_to='media/')
    eventDescription = models.CharField(max_length=255)
    eventChifeGuest = models.CharField(max_length=120)
    eventlocation = models.CharField(max_length=150)
    eventStartTime = models.CharField(max_length=25)
    eventDate = models.CharField(max_length=50)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    batch = models.CharField(max_length=10)
    passingYear = models.CharField(max_length=10)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100) 
    profileImage = models.ImageField(upload_to='media/')
