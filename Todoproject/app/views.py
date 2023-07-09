from django.shortcuts import render,redirect
from .models import userdata

def mainpage(request):
    data = userdata.objects.all()
    return render(request,'mainpage.html',{'data': data})

def formpage(request):
    if request.method=='GET':
        return render(request,'formpage.html')
    else:
        userdata(
            title=request.POST['title'],
            selectdata=request.POST['date'],
            taskdescription=request.POST['description']
        ).save()
        return redirect('mainpage')

def updatedata(request,id):
    nth = userdata.objects.get(id=id)
    if request.method=='GET':
        return render(request,'updatedata.html',{'nth':nth})
    else:
        nth.title=request.POST['title']
        nth.selectdata=request.POST['date']
        nth.taskdescription=request.POST['description']
        nth.save()
        return redirect('mainpage')

def deletedata(request,id):
    data=userdata.objects.get(id=id)
    data.delete()
    return redirect('mainpage')
