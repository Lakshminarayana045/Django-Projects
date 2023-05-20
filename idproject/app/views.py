from django.shortcuts import render,redirect
from .models import EmployeeData

def homepage(request):
    data = EmployeeData.objects.all()
    return render(request,'homepage.html',{'data':data})


def formpage(request):
    if request.method == 'GET':
        return render(request,'formpage.html')
    else:
        EmployeeData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email_id=request.POST['email'],
        salary=request.POST['salary'],
        company=request.POST['company'],
        mobile=request.POST['mobile'],
        locations=request.POST['locations']
        ).save()
        return redirect('homepage')

def detailspage(request,id):
    data = EmployeeData.objects.get(id=id)
    return render(request,'detailspage.html',{'data':data})

def deletepage(request,id):
    data = EmployeeData.objects.get(id=id)
    data.delete()
    return redirect('homepage')
