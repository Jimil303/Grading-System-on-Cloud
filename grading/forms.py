from django import forms
from django.db.models import fields
from grading.models import FacultyCredentials,StudentCredentials, course, messenger, semester

class Myform (forms.ModelForm):
 class Meta:
        model = FacultyCredentials
        fields = ['fac_id','name','phone','email','username', 'password']
        exclude =[]
        labels = {'fac_id':"Faculty ID",'name':"Full Name",'phone':"Phone no",'email':"e-mail",'username': "Username", 'password': "Password"}

class Myform2 (forms.ModelForm):
 class Meta:
        model = StudentCredentials
        fields = ['stu_id','name','phone','email','username', 'password']
        exclude =[]
        labels = {'stu_id':"Student ID",'name':"Full Name",'phone':"Phone no",'email':"e-mail",'username': "Username", 'password': "Password"}

class Myform3 (forms.ModelForm):
       class Meta:
              model = course
              fields = ['id','name','code','credits','kind']
              exclude = ['id']
              labels = {'name' : "Course Name",'code':"Course Code",'credits':"Credits",'kind':"Core/Elective"}

class Myform4(forms.ModelForm):
       class Meta:
              model = semester
              fields = ['year','type','number']
              exclude= []
              labels = {'year':"Year",'type':"Name",'number':"Semester Number"}

