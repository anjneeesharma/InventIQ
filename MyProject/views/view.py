from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from  MyProject.model import models
import myapp

import logging
logger = logging.getLogger(__name__)

@login_required(login_url="/login/")
def getEmployees(request):
	employess = models.getEmployee()
	emps = []
	for emp in employess.values():
		employee = {}
		employee['id'] =  emp['id']
		employee['email'] = emp['email']
		employee['name'] =  emp['name']
		employee['address'] =  emp['address']
		employee['mobile'] =  emp['mobile']
		employee['designation'] =  emp['designation']
		emps.append(employee)	
	emps = sorted(emps, key=lambda k: k['id']) 
	return  render(request,"getemployees.html",{'emps':emps})


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
	logger.debug('========================================================%%%%%%%%%%')
	logger.info('Something went wrong!')
	logger.info('========================================================%%%%%%%%%%%')
	employee = {}
	params = request.GET['id']
	params = params.split(' ')
	params = filter(None, params)  #will remove all empty string 
	employee['id']          = params[0]
	employee['name']        = params[1].split('=')[1]
	employee['email']       = params[2].split('=')[1]
	employee['address']     = params[3].split('=')[1]
	employee['mobile']      = params[4].split('=')[1]
	employee['designation'] = params[5].split('=')[1]
	return  render(request,"editemployee.html",{'employee':employee})







