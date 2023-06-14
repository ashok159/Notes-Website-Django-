from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

#this is used to implement error handling for the create view form class in views.py
#functions after the Meta class handle errors

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        #this widgets is a way to style forms directly from the backend
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
            'text': 'Write your note here:',
        }