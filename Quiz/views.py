from django.shortcuts import render
from . import forms as tforms

# Create your views here.
def create(request):
    def create_quiz_view(request):
        createQuizForm = tforms.CreateQuizForm()
        if request.method=='POST':
            createQuizForm=tforms.CreateQuizForm(request.POST)
            if createQuizForm.is_valid():        
                createQuizForm.save()
            else:
                print("form is invalid")
        return render(request,'Create_Quiz/Create_Quiz.html',{'createQuizForm':createQuizForm})
    return create_quiz_view(request)

def qa(request):
    return render(request, 'Teacher_QA/QA.html')

def summary(request):
    return render(request, 'Teacher_Quiz_Summary/Quiz-Summary.html')

def review(request):
    return render(request, 'Teacher_Review/Review.html')

def dashboard(request):
    return render(request, 'Teacher-Dashboard/Teacher-Dashboard.html')

def create_quiz_view(request):
    createQuizForm = tforms.CreateQuizForm()
    return render(request,'Create_Quiz/Create_Quiz.html',{'createQuizForm':createQuizForm})

