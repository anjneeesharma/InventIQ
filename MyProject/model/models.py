from myapp.models import Employee

def getEmployee():
	queryset = Employee.objects.all()
	return queryset

def submitaddemployee(name,email,address,mobile,designation):
	emp = Employee(name = name, email = email,address = address,mobile = mobile,designation = designation)
	emp.save()
