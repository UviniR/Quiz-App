from email.policy import default
from django.db import models
from signup.models import Student
from django.contrib.auth.models import User

class Quiz(models.Model):
   quiz_name = models.CharField(max_length=100, default='')
   instructions = models.CharField(max_length=600, default='')
   def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    correct = models.PositiveIntegerField()
    submitted_date = models.DateTimeField(auto_now=True)
    qCount = models.PositiveIntegerField(default=0)
