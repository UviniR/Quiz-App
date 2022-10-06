from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'Create_Quiz/Create_Quiz.html')

def qa(request):
    return render(request, 'Teacher_QA/QA.html')

def summary(request):
    return render(request, 'Teacher_Quiz_Summary/Quiz-Summary.html')

def review(request):
    return render(request, 'Teacher_Review/Review.html')

def dashboard(request):
    return render(request, 'Teacher-Dashboard/Teacher-Dashboard.html')