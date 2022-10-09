from email.policy import default
from django.db import models
from signup.models import Student
from django.contrib.auth.models import User

# Create your models here.
# class qna(models.Model):
#     Question = models.CharField(max_length=100)
#     Option1 = models.CharField(max_length=100)
#     Option2 = models.CharField(max_length=100)
#     Option3 = models.CharField(max_length=100)
#     Correct = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.Question
#
#
# class create(models.Model):
#     Name = models.CharField(max_length=50)
#     Instructions = models.CharField(max_length=250)
#     Passcode = models.CharField(max_length=4)

class Quiz(models.Model):
   quiz_name = models.CharField(max_length=100, default='')
   instructions = models.CharField(max_length=600, default='')
#    id = models.AutoField(primary_key=True, default=2)

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
