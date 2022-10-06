from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # mobile = models.CharField(max_length=20,null=False)
    email = models.EmailField('')
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')

   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
