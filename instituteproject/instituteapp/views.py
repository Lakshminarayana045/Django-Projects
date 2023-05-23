from django.shortcuts import render
from .models import CoursesData

def home_page(request):
    return render(request, 'home_page.html')

def contact_page(request):
    return render(request,'contact_page.html')

def services_page(request):
    courses = CoursesData.objects.all()
    return render(request, 'services_page.html',{'services':courses})

def feedback_page(request):
    return render(request, 'feedback_page.html')

def gallery_page(request):
    return render(request, 'gallery_page.html')
