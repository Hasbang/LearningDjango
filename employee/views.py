from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Employee




# Create your views here.


'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
'''
def index(request):
    MyEmployees = Employee.objects.all().values()
    template = loader.get_template('employee/index.html')
    context={
        'MyEmployees': MyEmployees
    }
    return HttpResponse(template.render(context, request))


def create(request):
    template = loader.get_template('employee/createpage.html')
    return HttpResponse(template.render( {}, request))


def createData(request):
    data1 = request.POST['name']
    data2 = request.POST['title']
    NewEmployee = Employee(name = data1 ,title= data2 ) 
    NewEmployee.save()
    return HttpResponseRedirect(reverse('index'))   


def delete(request,id):
    deleteemployee =Employee.objects.get(id=id)
    deleteemployee.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request,id):
    updateEmployee =Employee.objects.get(id=id)
    template = loader.get_template('employee/updatepage.html')
    context ={
        'Employee': updateEmployee
    }
    return HttpResponse(template.render(context, request))



def updateData(request, id):
    name = request.POST['name']
    title  = request.POST['title']
    updateEmployee =Employee.objects.get(id=id)
    updateEmployee.name=name 
    updateEmployee.title= title 
    updateEmployee.save()
    return HttpResponseRedirect(reverse('index'))  