from django.shortcuts import render
from django.http import HttpResponse
from .models import qna

# Create your views here.
def create(request):
    qa = qna.Question
    return render(request, 'Create_Quiz/Create_Quiz.html')

def qa(request):
    x = qna.objects.all()
    data = {
        'x' : x
    }
    return render(request, 'QA/QA.html', data)

def summary(request):
    return render(request, 'Quiz-Summary/Quiz-Summary.html')

def review(request):
    return render(request, 'Review/Review.html')

def dashboard(request):
    return render(request, 'Dashboard/Dashboard.html')