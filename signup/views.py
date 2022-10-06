from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = ''

# Create your views here.
def tsignup(request):
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into Quiz_teacher Values('{}','{}','{}','{}')".format(em, fn,ln, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'tsignup.html')

def ssignup(request):
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "insert into student_student Values('{}','{}','{}','{}')".format(em,fn, ln, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'ssignup.html')

