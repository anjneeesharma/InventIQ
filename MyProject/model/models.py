from myapp.models import Employee
from django.contrib.auth.models import User
from django.db.models import Q
import logging
logger = logging.getLogger(__name__)

def getEmployee(eid = None):
	if eid:
		queryset = Employee.objects.get(id=eid)
		return queryset
	else:
		queryset = Employee.objects.all()
		return queryset

def submitaddemployee(name,email,address,mobile,designation):
	try:
		emp = Employee(name = name, email = email,address = address,mobile = mobile,designation = designation)
	except psycopg2.IntegrityError:
		log.error("some error occured while inserting record")

	except Exception:
		log.error("some error occured while inserting record")
	else:
		emp.save()
		logger.info("Employee added successfully...........")



def submiteditemployee(eid,name,email,address,mobile,designation):
	#import pdb;pdb.set_trace()
	try:
		Employee.objects.filter(id=eid).update(name = name,email = email,address = address,mobile = mobile,designation = designation)
		'''
		or use this emp = Employee.objects.filter(id=eid)
					emp.name = 10 emp.save()
		'''
	except psycopg2.IntegrityError:
		log.error("some error occured while inserting record")

	except Exception:
		log.error("some error occured while inserting record....")
	else:
		logger.info("Employee added successfully...........")



def searchemployee(searchKey = None):
	try:
	    emp = Employee.objects.filter( Q(id__icontains=searchKey) | Q(name__icontains=searchKey) | Q(email__icontains=searchKey) | Q(address__icontains=searchKey) | Q(mobile__icontains=searchKey) | Q(designation__icontains=searchKey) )
	except Exception:
		logger.error("some error occured while retrieving record....")
	else:
	    return emp
	
	

def submitregisteruser(username,email,psw):
	if User.objects.filter(username=username).exists():
		return username
	user = User.objects.create_user(username = username,email = email,password = psw)
	return user



