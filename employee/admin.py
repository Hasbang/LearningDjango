from django.contrib import admin
from .models import Employee,Blogposts


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display =('name','title')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Blogposts)
