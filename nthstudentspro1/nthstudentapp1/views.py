from django.shortcuts import render,redirect
from .models import mainpage
def mainpagedata(request):
    cup=mainpage.objects.all()
    return render(request,'mainpage.html',{'cake':cup})

def addingstudents(request):
    if request.method =='GET':
        return render(request,'addingstudents.html')
    else:
        mainpage(
        firstname=request.POST['fname'],
        lastname=request.POST['lname'],
        coursename=request.POST['cname'],
        emailid=request.POST['email'],
        mobile=request.POST['mobile'],
        hometown=request.POST['htown'],
        qualification=request.POST['qualification'],
        percentage=request.POST['percentage'],
        passedoutyear=request.POST['year'],
        ).save()
        return redirect('mainpagedata')

def updatingstudents(request,id):
    rocky =mainpage.objects.get(id=id)
    if request.method=='GET':
        return render(request,'updatingstudents.html',{'rocket':rocky})
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
        return redirect('mainpagedata')
def deletingstudents(request,id):
    lucky=mainpage.objects.get(id=id)
    lucky.delete()
    return redirect('mainpagedata')
