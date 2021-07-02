from django import forms
from grading.models import FacultyCredentials,StudentCredentials, messenger

class Myform (forms.ModelForm):
 class Meta:
        model = FacultyCredentials
        fields = ['username', 'password', 'university', 'auth',]
        exclude =[]
        labels = {'username': "Username", 'password': "Password", 'university': "University", 'auth': "Infoadded"}
class Myform2 (forms.ModelForm):
 class Meta:
        model = StudentCredentials
        fields = ['username', 'password', 'university', 'auth',]
        exclude =[]
        labels = {'username': "Username", 'password': "Password", 'university': "University", 'auth': "Infoadded"}
