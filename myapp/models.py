from __future__ import unicode_literals

from django.db import models

# Create your models here.


#https://docs.djangoproject.com/en/1.10/ref/models/meta/   for field related info
#
class Employee(models.Model):
    name = models.CharField( blank=True,max_length=20)
    email = models.EmailField( blank=True)
    address = models.CharField( blank=True,max_length=20)
    mobile = models.CharField( blank=True,max_length=20)
    designation = models.CharField( blank=True,max_length=20)
    

