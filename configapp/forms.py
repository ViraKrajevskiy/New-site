import re

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



class NewsAdd(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','context','is_bool','category']
        widgets =  {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'category':forms.Select(attrs={'class':'form-control','rows':5}),
            }


    def clean_title(self):
        title = self.changed_data['title']
        if re.match(r'\d',title):
            raise ValueError('The name space is not started to number')
        return title


class NewsFrom:
    pass