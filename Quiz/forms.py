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

class AddQuestion(forms.ModelForm):
    quizID=forms.ModelChoiceField(queryset=models.Quiz.objects.all(),empty_label="quiz_name", to_field_name="id")
    class Meta:
        model = models.Question
        fields = ['quiz', 'question', 'option1', 'option2', 'option3', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
