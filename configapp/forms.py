from django import forms
from .models import *


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": 'form-control'}))

    context = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class": 'form-control', "rows": 5}))
    is_bool = forms.BooleanField(label='Опубликовано?', initial=True)

    category = forms.ModelChoiceField(empty_label='Выберите категории', label='Категория',
                                      queryset=Categories.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=40, label='Название', widget=forms.TextInput(attrs={"class": 'form-control'}))