from django import forms
from grading.models import FacultyCredentials

class Myform (forms.ModelForm):
    class Meta:
        model = FacultyCredentials
        feilds = ['username', 'password', 'university', 'auth',]
        exclude =[]
        labels = {'username': "Username", 'password': "Password", 'university': "University", 'auth': "Infoadded"}