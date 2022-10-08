from unicodedata import name
from django.shortcuts import render, redirect
from . import forms as tforms
from . import models as tmodel
from django.http import HttpResponseRedirect
from signup import models as signupModel

# Create your views here.
def create(request):
    def create_quiz_view(request):
        createQuizForm = tforms.CreateQuizForm()
        if request.method=='POST':
            createQuizForm=tforms.CreateQuizForm(request.POST)
            if createQuizForm.is_valid():        
                createQuizForm.save()
                createQuizForm = tforms.CreateQuizForm()
                return HttpResponseRedirect('qna')
            else:
                print("form is invalid")
        return render(request,'Create_Quiz/Create_Quiz.html',{'createQuizForm':createQuizForm})
    return create_quiz_view(request)
    

def qa(request):
    def add_question_view(request):
        questionForm = tforms.AddQuestion()
        if request.method=='POST':
            questionForm=tforms.AddQuestion(request.POST)
            if questionForm.is_valid():
                question=questionForm.save(commit=False)
                quiz=tmodel.Quiz.objects.get(id=request.POST.get('quiz_id'))
                question.quiz=quiz
                question.save() 
                questionForm = tforms.AddQuestion()      
            else:
                print("form is invalid")
            # return HttpResponseRedirect('/teacher/teacher-view-question')
        return render(request,'Teacher_QA/QA.html',{'questionForm':questionForm})
    return add_question_view(request)

def summary(request):
    return render(request, 'Teacher_Quiz_Summary/Quiz-Summary.html')

def review(request,pk):
    def view_question_view(request,pk):
        questions=tmodel.Question.objects.all().filter(quiz_id=pk)
        quiz = tmodel.Quiz.objects.get(id=pk)
        # for q in quiz:
        quizName = quiz.quiz_name
        instructions = quiz.instructions
        return render(request,'Teacher_Review/Review.html',{'questions':questions, 'quiz':quiz, 'quizName':quizName, 'instructions':instructions})
    return view_question_view(request,pk)

def dashboard(request):
    def teacher_dashboard(request):
        quizes = tmodel.Quiz.objects.all()
        teacher = signupModel.Teacher.objects.get(user_id = request.user.id)
        return render(request,'Teacher-Dashboard/Teacher_Dashboard.html',{'quizes':quizes, 'name': teacher})
    return teacher_dashboard(request)

def delete_exam_view(request,pk):
    quiz=tmodel.Quiz.objects.get(id=pk)
    quiz.delete()
    return HttpResponseRedirect('/quiz/dashboard')