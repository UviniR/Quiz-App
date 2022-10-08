# from django.shortcuts import render
# import mysql.connector as sql

# em = ''
# pwd = ''

# # Create your views here.
# def tlogin(request):
#     global em, pwd
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
#         cursor = m.cursor()
#         d = request.POST
#         for key, value in d.items():
#             if key == "email":
#                 em = value
#             if key == "password":
#                 pwd = value

#         c = "select * from Quiz_teacher where email='{}' and password='{}'".format(em, pwd)
#         cursor.execute(c)
#         t = tuple(cursor.fetchall())
#         if t == ():
#             return render(request, 'tlogin.html')
#         else:
#             return render(request, "Teacher-Dashboard/Teacher_Dashboard.html")

#     return render(request, 'tlogin.html')

# def slogin(request):
#     global em, pwd
#     if request.method == "POST":
#         m = sql.connect(host="localhost", user="root", passwd="", database='quizdb')
#         cursor = m.cursor()
#         d = request.POST
#         for key, value in d.items():
#             if key == "email":
#                 em = value
#             if key == "password":
#                 pwd = value

#         c = "select * from student where email='{}' and password='{}'".format(em, pwd)
#         cursor.execute(c)
#         t = tuple(cursor.fetchall())
#         if t == ():
#             return render(request, 'slogin.html')
#         else:
#             return render(request, "Teacher-Dashboard/Teacher_Dashboard.html")

#     return render(request, 'slogin.html')

