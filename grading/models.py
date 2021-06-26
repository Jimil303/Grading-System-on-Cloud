from django import db
from django.db import models


class FacultyCredentials(models.Model):
    username = models.CharField(db_column = 'username',max_length = 50, primary_key=True)
    password = models.CharField(db_column = 'password',max_length = 100)
    university = models.CharField(db_column = 'university',max_length = 100)
    auth = models.BooleanField(db_column = 'infoadded')

    class Meta:
        db_table = 'faculty_credentials'

class StudentCredentials(models.Model):
    username = models.CharField(db_column = 'username',max_length = 50, primary_key=True)
    password = models.CharField(db_column = 'password',max_length = 100)
    university = models.CharField(db_column = 'university',max_length = 100)
    auth = models.BooleanField(db_column = 'infoadded')

    class Meta:
        db_table = 'student_credentials'

class Universities(models.Model):
    name = models.CharField(db_column = 'name',max_length = 75,primary_key=True)
    username = models.CharField(db_column= 'username',max_length = 25,)
    password = models.CharField(db_column='password', max_length=100)

    class Meta:
        db_table = 'university'

class messenger(models.Model):
    sender = models.CharField(db_column = 'sender',max_length = 75)
    reciever = models.CharField(db_column='reciever',max_length=75)
    fileurl = models.CharField(db_column='fileurl', max_length=500)
    dated = models.DateField(db_column='date')
    time = models.TimeField(db_column='time')
    status = models.BooleanField(db_column='status')
    remarks = models.CharField(db_column='remarks',max_length=150)
    nameStudent = models.CharField(db_column= 'name',max_length=50)
    
    class Meta:
        db_table = 'messages'

# Create your models here.
