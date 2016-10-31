from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.template.loader import get_template 
from myapp.models import Employee
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
     




@login_required(login_url="/login/")
def home(request):
    return render(request,"home.html")


      
    
'''
lgn = get_template('login.html')
select_template() same as get_template(),  it takes a list of template names. It tries each name in order and returns the first template that exists.
after returning templating from these function need to be return ex Template.render


 context is provided, it must be a dict. in return 
 If request is provided, it must be an HttpRequest.
 
 
 
 TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/home/html/example.com',                                                // first try to search here 
            '/home/html/default',
        ],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            '/home/html/jinja2',                                                    // then it will try to serch
        ],
    },
]
 
 
 render==>calles==> render_to_string()==>calls==> HttpResponse
 
 render(request,template,context)
 
 loader   used for import templates   
'''    
     
