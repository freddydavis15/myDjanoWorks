from django.shortcuts import render
from django.http import HttpResponse
from .models import EmployeeDetails

# Create your views here.
def index(request):
    list_employee = EmployeeDetails.objects.all()
    date_employee ={'employee_records':list_employee}
    return render(request,"first.html",context=date_employee)
