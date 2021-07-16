from logging import PlaceHolder
from django import forms
from django.db.models import fields
from grading.models import FacultyCredentials,StudentCredentials, course, messenger, semester

class Myform (forms.ModelForm):
       fac_id = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Faculty ID'}))
       name = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
       phone = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
       email = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Email ID'}))
       username = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Username'}))
       password = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Password'}))
       class Meta:
              model = FacultyCredentials
              fields = ['fac_id','name','phone','email','username', 'password']
              exclude =[]
       

class Myform2 (forms.ModelForm):
       stu_id = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Student ID'}))
       name = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
       phone = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
       email = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Email ID'}))
       username = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Username'}))
       password = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Password'}))
       class Meta:
              model = StudentCredentials
              fields = ['stu_id','name','phone','email','username', 'password']
              exclude =[]
class Myform3 (forms.ModelForm):
       name = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Course Name'}))
       code = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Course Code'}))
       credits = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Credits'}))
       kind = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Core/Elective'}))
       class Meta:
              model = course
              fields = ['id','name','code','credits','kind']
              exclude = ['id']
              labels = {'name' : "Course Name",'code':"Course Code",'credits':"Credits",'kind':"Core/Elective"}

class Myform4(forms.ModelForm):
       year = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Year'}))
       type = forms.CharField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Semester Name'}))
       number = forms.IntegerField(label='', 
              widget=forms.TextInput(attrs={'placeholder': 'Semester Number'}))
       class Meta:
              model = semester
              fields = ['year','type','number']
              exclude= ['id']
              labels = {'year' : "Year",'type' : "Name", 'number':"Semester Number"}

