from django import forms
from django.db.models import fields
from grading.models import FacultyCredentials,StudentCredentials, course, messenger

class Myform (forms.ModelForm):
 class Meta:
        model = FacultyCredentials
        fields = ['id','name','phone','email','username', 'password']
        exclude =['id']
        labels = {'name':"Full Name",'phone':"Phone no",'email':"e-mail",'username': "Username", 'password': "Password"}

class Myform2 (forms.ModelForm):
 class Meta:
        model = StudentCredentials
        fields = ['id','name','phone','email','username', 'password']
        exclude =['id']
        labels = {'name':"Full Name",'phone':"Phone no",'email':"e-mail",'username': "Username", 'password': "Password"}

class Myform3 (forms.ModelForm):
       class Meta:
              model = course
              fields = ['id','name','code']
              exclude = ['id']
              labels = {'name' : "Course Name",'code':"Course Code"}