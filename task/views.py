from django.shortcuts import render,redirect
from task.forms import TaskForm
from task.models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    else:
        form = TaskForm()
    return render(request,'add_task.html',{'form' : form})

def show_task(request):
    data = TaskModel.objects.all()
    return render(request,'show_task.html',{'tasks':data})
def edit(request,id):
    form = TaskModel.objects.get(pk = id)
    show_form = TaskForm(instance=form)
    if request.method == 'POST':
        show_form = TaskForm(request.POST,instance=form)
        if show_form.is_valid():
            show_form.save()
            return redirect('show_task')
    return render(request,'add_task.html',{'form' : show_form})
def delete(request,id):
    form = TaskModel.objects.get(pk = id)
    form.delete()
    return redirect('show_task')
    