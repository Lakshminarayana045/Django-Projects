"""fakerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.generatingData),
    path('Fetch',views.FetchData, name='FetchData'),
    path('Hyderabad',views.Hyderabad,name='Hyderabad'),
    path('Pune',views.Pune,name='Pune'),
    path('Bangalore',views.Bangalore,name='Bangalore'),
    path('Chenni',views.Chenni,name='Chenni'),
    path('',views.mainpage,name='mainpage')
]
