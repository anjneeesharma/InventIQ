ITS ALL ABOUT PROJECT

pip install virtualenv
py -m virtualenv myvirtual
myvirtual\Scripts\activate
pip install django==1.10
django-admin startproject MyProject
cd MyProject
python manage.py startapp myapp

===================================================================================================================================
python       2.7
Django       1.10 
PostgreSQL   9.5.4
window       7 32bit
github
emailID  anjnee.k.sharma@gmail.com

=============================================================================== 
Todays Task
install everything and configure
create home page
===============================================================================
GIT FOR WINDOW

https://git-for-windows.github.io/



==============================================================================

STATIC FILES

https://docs.djangoproject.com/en/1.10/intro/tutorial06/

https://docs.djangoproject.com/en/1.10/howto/static-files/



django.contrib.staticfiles===>

 it collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production.




 from django.conf.urls.static import static            //add in url.py




======================================================================================================================
ADMIN interface

python manage.py makemigrate
python manage.py migrate
python manage.py createsuperuser

user             anjnee
email address    anjnee.k.sharma@gmail.com
password         password123



REGISTER class in admin interface

in MYAPP/ADMIN.PY
from models import *




=====================================================================================================================
CREATE MODEL AND DATABASE CONNECTIVITY

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testDB',                      
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




InventQ/myapp/models.py      // write your all  mapping classes here
pip install psycopg2


python manage.py makemigrations    myapp
python manage.py migrate           myapp         //if u give myapp at last table name will start with your appname the underscore      


python manage.py migrate                       // after changing anything to database






===================================================================================================================
DJANGO-ORM

python manage.py shell      // you can run python program also here




Writing action functions==>its 3 argument modeladmin, request, queryset)











==================================================================================================================


OTHER DJANGO CONCEPT

======================================================================================================================================

A view is a callable which takes a request and returns a response

USE OF CLASS BASED VIEW
You can subclass a class and refine methods like get_context_data for specific cases, and leave the rest as-is. You can't do that with functions.

Django provides an example of some classes which can be used as views

Class-based views provide an alternative way to implement views as Python objects instead of functions. They do not replace function-based views, but have certain differences 
and advantages when compared to function-based views:

like in URL.py we can not use object of a class but using class-based we can use

history of views who came first

    In the beginning there was only the view function
    Function-based generic views
    The problem with function-based generic views is that while they covered the simple cases well, 
    there was no way to extend or customize them beyond some simple configuration options, limiting their usefulness in many
    real-world applications.
     
    Class-based generic views were created with the same objective as function-based generic views
     
     
 EXAMPLE
 SIMPLE VIEW
      
    from django.http import HttpResponse
    def my_view(request):
        if request.method == 'GET':
            # <view logic>
        return HttpResponse('result')   
    
    
 =============================================================================   
 CLASS BASED VIEW
 
  from django.http import HttpResponse
  from django.views import View

  class MyView(View):
      def get(self, request):
          # <view logic>
            return HttpResponse('result')  
    
    
   as_view()===>Django’s URL resolver expects to send the request and associated arguments to a callable function, 
   not a class, class-based views  so as_view() will convert your view request to simple request.it calles  dispatch
   that will decide is it post or get request.
   
   
    
    
    # urls.py
    from django.conf.urls import url
    from myapp.views import MyView

   urlpatterns = [
       url(r'^about/$', MyView.as_view()),
   ]   
    
 ==============================================================================
 USE OF CLASS BASED VIEW(overriding)    
 
 
from django.http import HttpResponse
from django.views import View

class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
    
 
 You can override that in a subclass:
 
 urlpatterns = [
    url(r'^about/$', GreetingView.as_view(greeting="G'day")),  //we can pass value for class variable
]
 
 
 
using mixins 
 Mixins are a form of multiple inheritance where behaviors and attributes of multiple parent classes can be combined.
 Mixins are an excellent way of reusing code across multiple classes
    
    
 =============================================================================   
Decorating class-based views

The simplest way of decorating class-based views is to decorate the result of the as_view() method. 
The easiest place to do this is in the URLconf where you deploy your view:


from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

from .views import VoteView

urlpatterns = [
    url(r'^about/$', login_required(TemplateView.as_view(template_name="secret.html"))),
    url(r'^vote/$', permission_required('polls.can_vote')(VoteView.as_view())),
]


=============================================================================
TEMPLATE

TemplateView
Renders a given template, with the context containing parameters captured in the URL.
url(r'^login/$', TemplateView.as_view(template_name="login.html"))     //from URL to Template no view

{% extends "admin/base_site.html" %}       // all basic setting from same as admin



==============================================================================
 (?P<name>pattern), where name is the name of the group and pattern is some pattern to match.

url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),  // "year" is name and [0-9]{4} should be match


url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail)


 The captured values are passed to view functions as keyword arguments rather than positional arguments
 
 
 {month:12,day:10}    // named argument will be passed   and its pass positional arguments
 
 ==================================================================================
 some extra argument other than url
 
 urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
]
 

will call

views.year_archive(request, year='2005', foo='bar') 
==============================================================================
urlpatterns = [
    #...
    url(r'^articles/([0-9]{4})/$', views.year_archive, name='news-year-archive'),
    #...
]


name='news-year-archive'     //call reverse url  used like   return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

                              or it can be used other than view matching  like in template or form
==============================================================================
For instance, you might need to create a new view that does everything a previous one does, but you need to include extra variable in the context. 
Subclass the original view and override the get_context_data method.

t makes for an ease-of-override




=====================================================================================
USER

python manage.py changepassword *username* password   // to changed password if not give username then it will changed password of loged in user


or 

call method     set_password():

from django.contrib.auth.models import User
u = User.objects.get(username='john')
u.set_password('new password')
u.save()




or 



if request.user.is_authenticated:
    # Do something for authenticated users.
    ...
else:
    # Do something for anonymous users.
    ...

============================================================================================
GIT IN DETAILS


first time



    git add db.sqlite3
    git add InventQ/
    git add  manage.py
    git add  myapp/
    git add  MyProject/
    git add  templates/
    git status
    cls
    git add --all
    git commit -am "First commit"
    git remote add origin https://github.com/anjneeesharma/InventIQ.git
    git push -u origin master
   
   -----------------------------
   second time own word

   git add   for undo git reset <file>




























