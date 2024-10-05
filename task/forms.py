from task.models import Task
from django import forms
from .models import Category, Priority


class TaskFilterForm(forms.Form):
    search_task = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={'placeholder': 'Поиск по задачам'}),
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Категория',
    )
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        required=False,
        label='Приоритет',
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'