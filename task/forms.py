from django import forms
from task.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'taskAssignDate' : forms.DateInput(attrs={'type' : 'date'})
        }