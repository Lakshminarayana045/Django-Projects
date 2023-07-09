from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Appointment,AllAppointments

# Create your views here.


def HomePage(request):
    return render(request,'index.html')

def admin_view(request):
    return render(request,'adminpage.html')

def patient_view(request):
    return render(request,'patientpage.html')

def admin_signup_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.is_active = True
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            return redirect('admin')
    return render(request,'admin_signup.html')


def admin_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('admin_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request,'admin_login.html')

def patient_signup_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.is_active = True
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.save()
            return redirect('patient')
    return render(request,'patient_signup.html')

def patient_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('patient_dashboard')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request,'patient_login.html')

def admin_dashboard(request):
    user_name = request.user.first_name
    appointment = Appointment.objects.all()
    return render(request,'admin_dashboard.html',{'user':user_name,'appointment':appointment})

def patient_dashboard(request):
    user_name = request.user.first_name
    return render(request,'patient_dashboard.html',{'user':user_name})


def patient_appointment(request):
    if request.method == 'GET':
        user_name = request.user.first_name
        return render(request,'patient_appointment.html',{'user':user_name})
    else:
        Appointment(
            name = request.POST['name'],
            age = request.POST['age'],
            gender  =request.POST['gender'],
            blood_group = request.POST['blood_group'],
            address = request.POST['address'],
            city = request.POST['city'],
            branch = request.POST['branch'],
            date = request.POST['date']
        ).save()
        AllAppointments(
            name = request.POST['name'],
            age = request.POST['age'],
            gender  =request.POST['gender'],
            blood_group = request.POST['blood_group'],
            address = request.POST['address'],
            city = request.POST['city'],
            branch = request.POST['branch'],
            date = request.POST['date']
        ).save()
        return redirect('patient_dashboard')
    
def appointment_reject(request,id):
    data = Appointment.objects.get(id=id)
    data1 = AllAppointments.objects.get(id=id)
    data1.status = False
    data.delete()
    return redirect('admin_dashboard')

def appointment_accept(request,id):
    data = Appointment.objects.get(id=id)
    data1 = AllAppointments.objects.get(id=id)
    data.status = True
    data1.status = True
    data.save()
    data1.save()
    return redirect('admin_dashboard')

def check_status(request):
    name1 = request.user.first_name
    data = AllAppointments.objects.get(name=name1)
    stat = data.status
    return render(request,'status.html',{'status':stat})

def admin_logout_view(request):
    logout(request)
    return redirect('admin')

def patient_logout_view(request):
    logout(request)
    return redirect('patient')
