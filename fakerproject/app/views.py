from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import EmployeeData
import faker
fa=faker.Faker()

def mainpage(request):
    return render(request,'mainpage.html')


def generatingData(request):
    for i in range(100):
        EmployeeData(
        first_name=fa.first_name(),
        last_name=fa.last_name(),
        emailid=fa.email(),
        mobile=fa.random_element(elements=(8179565167,9010607010,9603091167)),
        address=fa.address(),
        company=fa.random_element(elements=('TCS','IBM','WIPRO','NTH')),
        salary=fa.random_element(elements=(30000,40000,50000,60000)),
        location=fa.random_element(elements=('Hyderabad','Pune','Bangalore','Chenni'))
        ).save()
    return redirect("FetchData")

def FetchData(request):
    data=EmployeeData.objects.all()
    return render(request,'fetchData.html',{'nth':data})

def Hyderabad(request):
    if request.method == 'GET':
        hyddata = EmployeeData.objects.filter(location='Hyderabad')
        return render(request,'hyd.html',{'hyddata':hyddata})
    else:
        val = request.POST['com']
        hyddata = EmployeeData.objects.filter(location='Hyderabad') & EmployeeData.objects.filter(company=val)
        return render(request,'hyd.html',{'hyddata':hyddata})

def Pune(request):
    if request.method == 'GET':
        punedata = EmployeeData.objects.filter(location='Pune')
        return render(request,'pune.html',{'punedata':punedata})
    else:
        val = request.POST['com']
        punedata = EmployeeData.objects.filter(location='Pune') & EmployeeData.objects.filter(company=val)
        return render(request,'pune.html',{'punedata':punedata})

def Bangalore(request):
    if request.method == 'GET':
        bandata = EmployeeData.objects.filter(location='Bangalore')
        return render(request,'ban.html',{'bandata':bandata})
    else:
        val = request.POST['com']
        bandata = EmployeeData.objects.filter(location='Bangalore') & EmployeeData.objects.filter(company=val)
        return render(request,'ban.html',{'bandata':bandata})

def Chenni(request):
    if request.method == 'GET':
        chedata = EmployeeData.objects.filter(location='Chenni')
        return render(request,'che.html',{'chedata':chedata})
    else:
        val = request.POST['com']
        chedata = EmployeeData.objects.filter(location='Chenni') & EmployeeData.objects.filter(company=val)
        return render(request,'che.html',{'chedata':chedata})
