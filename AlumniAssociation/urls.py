"""AlumniAssociation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Alumni import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home, name="home"),
path('login', views.login, name="login"),
path('registration', views.registration, name="registration"),
path('profile', views.profile, name="profile"),
path('edit_profile', views.edit_profile, name="edit_profile"),
path('job_post', views.job_post, name="job_post"),
path('event_post', views.event_post, name="event_post"),
path('event_view', views.event_view, name="event_view"),
path('job_view', views.job_view, name="job_view"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
