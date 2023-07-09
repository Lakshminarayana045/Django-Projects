from django.shortcuts import render,HttpResponse,redirect
from.models import student
from django.db import connection

def form_data(request):
    data=student.objects.all()
    if request.method=='GET':
        return render(request,'form.html',{'data':data})

    else:
        student(
        Name=request.POST['name'],
        roll_no=request.POST['rollno'],
        dob=request.POST['dob'],
        marks_percentage=request.POST['mpercentage'],
        class_group=request.POST['cgroup'],
        father_name=request.POST['fname'],
        ).save()
        return HttpResponse('your data is successfully saved')

def update_data(request,id):
    data=student.objects.get(id=id)
    if request.method=='GET':
        return render(request,'updatedata.html',{'data':data})
    else:
        data.Name=request.POST['name']
        data.roll_no=request.POST['rollno']
        data.dob=request.POST['dob']
        data.marks_percentage=request.POST['mpercentage']
        data.class_group=request.POST['cgroup']
        data.father_name=request.POST['fname']
        data.save()
        return redirect('form')

def clear_data(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('form')

def overall_pass_percentage(request):
    # calculate overall pass percentage
    total_students = student.objects.all().count()
    passed_students = student.objects.filter(marks_percentage__gte=40).count()
    pass_percentage = (passed_students / total_students) * 100
    print(pass_percentage)

    # return response
    return HttpResponse("percentage is" + str(pass_percentage))
