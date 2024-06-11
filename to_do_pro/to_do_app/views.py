from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    tasks = task.objects.all()
    form = taskForm

    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    constext = {'tasks':tasks,'form':form}
    return render(request,'home.html',constext)
# Create your views here.

def updateTask(request,pk):
    tasks = task.objects.get(id=pk)
    form = taskForm(instance=tasks)
    if request.method == 'POST':
        form = taskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    constext = {'form':form}
    return render(request,'Edit.html',constext)

def deleteTask(request,pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    constext = {'item':item}
    return render(request,'delete.html',constext)