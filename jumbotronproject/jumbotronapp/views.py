from django.shortcuts import render,redirect
from .models import studentsdata

def form(request):
    if request.method == 'GET':
        return render(request,'form.html')

    else:
        studentsdata(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        course_name=request.POST['cname'],
        mobile=request.POST['mobile'],
        email=request.POST['email'],
        qualification=request.POST['qua'],
        passoutyear=request.POST['poy']
        ).save()
        return redirect(mainpage)



def mainpage(request):
    return render(request,'mainpage.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def c(request):
    return render(request,'c.html')

def mysql(request):
    return render(request,'mysql.html')
