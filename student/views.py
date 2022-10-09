from django.shortcuts import render,redirect
from django.http import HttpResponse
from Quiz import models as qmodel
from signup import models as signupModel
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='slogin')
@user_passes_test(is_student)  
def student_d(request):
    def student_dashboard(request):
        quizes = qmodel.Quiz.objects.all()
        student = signupModel.Student.objects.get(user_id = request.user.id)
        return render(request,'student_dashboard.html',{'quizes':quizes, 'name': student})
    return student_dashboard(request)

@login_required(login_url='slogin')
@user_passes_test(is_student)  
def attempt(request,pk):
    quiz = qmodel.Quiz.objects.get(id=pk)
    questions = qmodel.Question.objects.all().filter(quiz_id=pk)
    if request.method=='POST':
        pass
    response= render(request,'attempt.html',{'quiz':quiz,'questions':questions})
    response.set_cookie('quiz',quiz.id)
    return response

@login_required(login_url='slogin')
@user_passes_test(is_student)  
def grades(request):
    student = signupModel.Student.objects.get(user_id = request.user.id)
    results = qmodel.Result.objects.all().filter(student = student)
    return render(request, 'grades.html',{'results': results})

def stud_logout_view(request):
    logout(request)
    return redirect('../')

@login_required(login_url='slogin')
@user_passes_test(is_student)
def calculate_marks(request):
    if request.COOKIES.get('quiz') is not None:
        quiz_id = request.COOKIES.get('quiz')
        quiz = qmodel.Quiz.objects.get(id=quiz_id)
        total_marks=0
        questions=qmodel.Question.objects.all().filter(quiz=quiz)
        for i in range(len(questions)):
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + 1
        student = signupModel.Student.objects.get(user_id=request.user.id)
        result = qmodel.Result()
        result.correct=total_marks
        result.exam=quiz
        result.student=student
        result.qCount=len(questions)
        result.save()
        return HttpResponseRedirect('grades')
