from django.shortcuts import render,redirect
from .models import CommentData
import datetime as dt

def homepage(request):
    data = CommentData.objects.all()  # CommentData.objects.all().order_by('-id')
    lst = []
    for i in data:
        lst.insert(0,i)
    if request.method == 'GET':
        return render(request,'homepage.html',{'data':lst})
    else:
        CommentData(
        comment = request.POST['com'],
        date = dt.datetime.now()
        ).save()
        return redirect('homepage')

def deletepage(request,id):
    data=CommentData.objects.get(id=id)
    data.delete()
    return redirect('homepage')
