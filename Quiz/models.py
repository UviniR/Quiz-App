from django.db import models

# Create your models here.
class qna(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Correct = models.CharField(max_length=10)

    def __str__(self):
        return self.Question


class create(models.Model):
    Name = models.CharField(max_length=50)
    Instructions = models.CharField(max_length=250)
    Passcode = models.CharField(max_length=4)

class Quiz(models.Model):
    Name=models.CharField(max_length=20)
