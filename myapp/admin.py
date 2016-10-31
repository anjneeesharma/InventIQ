from django.contrib import admin
from models import *
from django.db import models

#admin.site.add_action(export_selected_objects)  //this is for adding action i.e export_selected_objects being called
admin.site.register(Employee)



'''
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']

admin.site.register(Employee, EmployeeAdmin)
'''










# This ia example of bulk updation from admin only so all comman task can be written
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):              # __unicode__ on Python 2
        return self.title



# we can write action function also for that task will be called when condition will be triggered from admin

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"











