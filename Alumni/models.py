from django.db import models

# Create your models here.


class JobCircular (models.Model):
    jobTitle = models.CharField(max_length=100)
    jobDescriptio = models.CharField(max_length=255)
    jobPostion = models.CharField(max_length=100)
    jobNuture = models.CharField(max_length=50)
    jobExperiance = models.CharField(max_length=50)
    workPlace = models.CharField(max_length=120)
    educationalRequierments = models.CharField(max_length=150)
    mustRequierdSkills = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    jobImageBanner = models.ImageField()
    deadline = models.CharField(max_length=30)


class EventPost(models.Model):
    eventTitle = models.CharField(max_length=100)
    eventImage = models.ImageField()
    eventDescription = models.CharField(max_length=255)
    eventChifeGuest = models.CharField(max_length=120)
    eventlocation = models.CharField(max_length=150)
    eventStartTime = models.CharField(max_length=25)
    eventDate = models.CharField(max_length=50)
