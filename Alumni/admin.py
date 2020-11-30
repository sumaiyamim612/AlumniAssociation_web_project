from django.contrib import admin
from .models import JobCircular, EventPost, Profile
# Register your models here.

admin.site.register(JobCircular)
admin.site.register(EventPost)
admin.site.register(Profile)
