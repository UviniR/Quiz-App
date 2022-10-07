# from django.shortcuts import render
# import mysql.connector as sql

# fn = ''
# ln = ''
# em = ''
# pwd = ''

# # Create your views here.
# def tsignup(request):
#     global fn, ln, em, pwd
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
#         cursor = m.cursor()
#         d = request.POST
#         for key, value in d.items():
#             if key == "first_name":
#                 fn = value
#             if key == "last_name":
#                 ln = value
#             if key == "email":
#                 em = value
#             if key == "password":
#                 pwd = value

#         c = "insert into Quiz_teacher Values('{}','{}','{}','{}')".format(em, fn,ln, pwd)
#         cursor.execute(c)
#         m.commit()

#     return render(request, 'tsignup.html')

# def ssignup(request):
#     global fn, ln, em, pwd
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
#         cursor = m.cursor()
#         d = request.POST
#         for key, value in d.items():
#             if key == "first_name":
#                 fn = value
#             if key == "last_name":
#                 ln = value
#             if key == "email":
#                 em = value
#             if key == "password":
#                 pwd = value

#         c = "insert into student_student Values('{}','{}','{}','{}')".format(em,fn, ln, pwd)
#         cursor.execute(c)
#         m.commit()

#     return render(request, 'ssignup.html')


from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta


def teacher_signup_view(request):
    userForm=forms.TeacherUserForm()
    teacherForm=forms.TeacherForm()
    mydict={'userForm':userForm,'teacherForm':teacherForm}
    if request.method=='POST':
        userForm=forms.TeacherUserForm(request.POST)
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if userForm.is_valid() and teacherForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            teacher=teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
        return HttpResponseRedirect('../login/tlogin')
    return render(request,'tsignup.html',context=mydict)



def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


