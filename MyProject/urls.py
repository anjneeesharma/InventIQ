
"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import TemplateView
from views.view import getEmployees,submitaddemployee,editemployee

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inventq/', include('myapp.urls')),

    # view given by django only we need to import and register
    url(r'^login/$', views.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$',views.logout,{'template_name': 'log_out.html'}, name='logout'),
    url('^change-password/$', views.password_change,{'template_name': 'change-password.html'},name='change-password'),
    url(r'^change-password/$', views.password_change, {'template_name': 'change-password.html'}, name='change-password.html'),
    url(r'^password-change-done/$', views.password_change_done,  {'password-change-done': 'password-change-done.html'}, name='password_change_done'),

    
    # Develop URL for specific need
    url(r'^home/$', TemplateView.as_view(template_name="home.html")),
    url(r'^getemployees/$', getEmployees,name='getemployee'),
    url(r'^addemployee/$', TemplateView.as_view(template_name="addemployee.html")),
    url(r'^editemployee/$', editemployee, name="editemployee"),
    #url(r'^submiteditemployee/$', submiteditemployee,name="submiteditemployee"),
    url(r'^submitaddemployee/$', submitaddemployee,name="submitaddemployee"),

    
    
]
