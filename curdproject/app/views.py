from django.shortcuts import render,redirect
from .models import StudentsData

def homepage(request):
    data = StudentsData.objects.all()
    return render(request,'homepage.html',{'data':data})
def adddata(request):
    if request.method=='GET':
        return render(request,'adddata.html')
    else:
        StudentsData(
        first_name=request.POST['fname'],
        mobile=request.POST['mob'],
        gmail=request.POST['gmail'],
        location=request.POST['loc']
        ).save()
        return redirect("homepage")
def update(request, id):
    data=StudentsData.objects.get(id=id)
    if request.method=='GET':
        return render(request,'update.html',{'lucky':data})
    else:
        data.first_name=request.POST['fname']
        data.mobile=request.POST['mob']
        data.gmail=request.POST['gmail']
        data.location=request.POST['loc']
        data.save()
        return redirect("homepage")

def delete(request,id):
    data=StudentsData.objects.get(id=id)
    data.delete()
    return redirect('homepage')
