from .models import Task
from .models import City
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите цель заметки'
        }),
            'task': Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Напишите описание заметки'
        }),
        }

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']