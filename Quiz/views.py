from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    return render(request, 'Create_Quiz/Create_Quiz.html')

def qna(request):
    return render(request, 'QA/QA.html')

def summary(request):
    return render(request, 'Quiz-Summary/Quiz-Summary.html')

def review(request):
    return render(request, 'Review/Review.html')
