from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from . import models

class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = ['quiz_name', 'instructions']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
    # quiz_name = forms.CharField(max_length=50)
    # instructions = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))

class AddQuestion(forms.Form):
    class Meta:
        model = models.Question
