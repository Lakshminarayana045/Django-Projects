from django.contrib import admin
from .models import EmpData

class AdminEmpData(admin.ModelAdmin):
    class Meta:
        model = EmpData
        field = ['__all__']


admin.site.register(EmpData,AdminEmpData)

