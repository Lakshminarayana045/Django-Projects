from django.shortcuts import render,redirect
from .models import StudentData

def mainpage(request):
    if request.method == 'GET':
        data=StudentData.objects.all()
        return render(request,'mainpage.html',{'data':data})
    else:
        StudentData(
            firstname=request.POST['fname'],
            lastname=request.POST['lname'],
            coursename=request.POST['cname'],
            emailid=request.POST['email'],
            mobile=request.POST['mobile'],
            hometown=request.POST['htown'],
            qualification=request.POST['qualification'],
            percentage=request.POST['percentage'],
            passedoutyear=request.POST['pyear']
        ).save()
        return redirect('mainpage')
def updatepage(request,id):
    rocky = StudentData.objects.get(id=id)
    if request.method=='GET':
        return render(request,'updatepage.html',{'rocket':rocky})
    else:
        rocky.firstname=request.POST['fname']
        rocky.lastname=request.POST['lname']
        rocky.coursename=request.POST['cname']
        rocky.emailid=request.POST['email']
        rocky.mobile= request.POST['mobile']
        rocky.htown=request.POST['htown']
        rocky.qualification=request.POST['qualification']
        rocky.percentage=request.POST['percentage']
        rocky.passedout=request.POST['year']
        rocky.save()
        return redirect('mainpage')
