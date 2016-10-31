from django.conf.urls import url
from django.contrib import admin
from myapp.views.home import home
# for logout and login
from django.contrib.auth.views import login,logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [

    url(r'^home/$', home, name='home'),
           

]
