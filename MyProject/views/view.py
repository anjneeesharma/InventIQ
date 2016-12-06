from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from  MyProject.model import models
#from tasks import sendEmail
import myapp

import logging
logger = logging.getLogger(__name__)

@login_required(login_url="/login/")
def getEmployees(request):
	employess = models.getEmployee().order_by('id')
	page = request.GET.get('page')
	try:
		paginator = Paginator(employess, 5)
		page = request.GET.get('page')
		employess = paginator.page(page)
		print employess
	except PageNotAnInteger:
		employess = paginator.page(1)
	except EmptyPage:
		employess = paginator.page(paginator.num_pages)
	return  render(request,"getemployees.html",{'employess':employess})


@login_required(login_url="/login/")
def submitaddemployee(request):
	name = 	request.GET['name']
	email = request.GET['email']
	address = request.GET['address']
	mobile = request.GET['mobile']
	designation = request.GET['designation']
	try:
		models.submitaddemployee(name,email,address,mobile,designation)
	except Exception, e:
		print "DB exception occured"
		return  render(request,"addemployee.html",{'failed':True})
	return  render(request,"addemployee.html",{'success':True})



@login_required(login_url="/login/")
def editemployee(request):
	#import pdb;pdb.set_trace()
	employee = {}
	eid = request.GET['id']
	emp = models.getEmployee(eid = eid)
	employee['id']          = emp.id
	employee['name']        = emp.name
	employee['email']       = emp.email
	employee['address']     = emp.address
	employee['mobile']      = emp.mobile
	employee['designation'] = emp.designation
	return  render(request,"editemployee.html",{'employee':employee})




@login_required(login_url="/login/")
def submiteditemployee(request):
	eid          = request.GET['ID']
	name         = 	request.GET['name']
	email        = request.GET['email']
	address      = request.GET['address']
	mobile       = request.GET['mobile']
	designation  = request.GET['designation']


	try:
		models.submiteditemployee(eid,name,email,address,mobile,designation)
	except Exception, e:
		print "DB exception occured"
		return  render(request,"editemployee.html",{'failed':True})
	return  render(request,"editemployee.html",{'success':True})


@login_required(login_url="/login/")
def searchemployee(request):
	searchKey = request.GET.get('searchKey')
	employees = models.searchemployee(searchKey = searchKey).order_by('id')
	n_recordfound = len(employees)
	try:
		paginator = Paginator(employees, 5)
		page = request.GET.get('page',1)
		employees = paginator.page(page)
	except PageNotAnInteger:
		employees = paginator.page(1)
	except EmptyPage:
		employees = paginator.page(paginator.num_pages)
	n_page = n_recordfound/5
	return  render(request,"searchemployee.html",{'employees':employees,'n_recordfound':n_recordfound,'searchKey':searchKey,'page':page,'n_page':n_page})


@login_required(login_url="/login/")
def submitregisteruser(request):
	username = request.GET['username']
	email = request.GET['email']
	psw = request.GET['psw']
	confirmpsw = request.GET['confirmpsw']
	registeredUser = models.submitregisteruser(username,email,psw)
	logger.info(registeredUser)
	#sendEmail(email)
	send_mail('Dummy Subject','Here is the Dummy message.','anjnee.k.sharma@gmail.com',['anjneesharma@gmail.com'],fail_silently=False,)
	return  render(request,"registeruser.html",{'success':registeredUser})




