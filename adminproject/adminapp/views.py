from django.shortcuts import render,redirect
from .models import EmpData

def datapage(request):
    data = EmpData.objects.all()
    return render(request,'display.html',{'data':data})

def deletepage(request,id):
    data = EmpData.objects.get(id=id)
    data.delete()
    return redirect('datapage')

def homepage(request):
    return render(request,'homepage.html')