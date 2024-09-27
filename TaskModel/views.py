from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        taskmodel_form = forms.TaskModelForm(request.POST)
        if taskmodel_form.is_valid():
            taskmodel_form.save()
            return redirect('homepage')

    else:
        taskmodel_form = forms.TaskModelForm()
    return render(request,'add_taskmodel.html',{'form': taskmodel_form})


def edit_task(request,id):
    task = models.TaskModel.objects.get(pk=id)
    taskmodel_form = forms.TaskModelForm(instance=task)

    if request.method == 'POST':
        taskmodel_form = forms.TaskModelForm(request.POST,instance=task)
        if taskmodel_form.is_valid():
            taskmodel_form.save()
            return redirect('homepage')

    
    return render(request,'add_taskmodel.html',{'form': taskmodel_form})

def delete_task(request,id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')

def complate_task(request,id):
    task = models.TaskModel.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('homepage')
    
