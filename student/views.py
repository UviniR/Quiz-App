from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_d(request):
    return render(request, 'student_dashboard.html')

def attempt(request):
    return render(request, 'attempt.html')

def grades(request):
    return render(request, 'grades.html')