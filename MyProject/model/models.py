from models import Employee

def getEmployee():
	queryset = Employee.objects.all()
	return queryset