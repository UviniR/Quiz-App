# Quiz App 🧑‍🏫
This is an online quiz platform which allows the teachers to create quizes and students to attempt them at their comfort zones.  
### Web App User Interface 

### Functionality 
  #### Teacher
  * Create an account as a teacher
  * After login can view a dashboard with all the available quizes
  * Add new questions to the existing quize
  * Create new quizes and add questions
  * Review created quizes
  * Delete quizes
  #### Student
  * Create an account as a student
  * After login can view a dashboard with all the available quizes
  * Attempt any quiz
  * View grades of all the attempted quizes
 *** 
### How to Run the Project 
  * Install Python 
  * Install `Django 4.1.2`
  
  ```
  pip install Django
  ```
  * Download the poroject to your local machine 
  * Open a terminal from the project directory and run the below commands
  
  ```
  pip install mysql-connector-python-rf
  pip install pymysql
  pip install django-widget-tweaks
  ```
  
  * Open `settings.py` and add `widget-tweaks` to `INSTALLED_APPS` as below;

  ```python
  INSTALLED_APPS += [
    'widget_tweaks',
  ]
  ```
 * Create a php MySQL Database as `quizdb`
 * Run the following commands to do the database migrations

 ```
 python manage.py makemigrations
 python manage.py migrate
```
 * Run the server
 
 ```
 python manage.py runserver
 ```
 * Now you can view the project using the below URL

```
http://127.0.0.1:8000/
```
***
### Further Work
 * Include an admin panel
 * Let teachers view the grades of students
 * Let students view the correct answers 

