from os import truncate
from django import db
from django.db import models
from django.db.models.fields import CharField

class admin (models.Model):
    id = models.IntegerField(db_column='id')
    username = models.CharField(db_column='username',max_length=50,primary_key=True)
    password = models.CharField(db_column='password',max_length=50)
    university = models.CharField(db_column='university',max_length=100)
    
    class Meta:
        db_table = 'admin1'

class FacultyCredentials(models.Model):
    fac_id = models.IntegerField(db_column='id')
    name = models.CharField(db_column='name',max_length=50)
    phone = models.IntegerField(db_column='phone')
    email = models.CharField(db_column='email',max_length=100)
    username = models.CharField(db_column = 'username',max_length = 50,primary_key=True)
    password = models.CharField(db_column = 'password',max_length = 50)

    class Meta:
        db_table = 'faculty'

class StudentCredentials(models.Model):
    stu_id = models.IntegerField(db_column='id')
    name = models.CharField(db_column='name',max_length=50)
    phone = models.IntegerField(db_column='phone')
    email = models.CharField(db_column='email',max_length=100)
    username = models.CharField(db_column = 'username',max_length = 50,primary_key=True)
    password = models.CharField(db_column = 'password',max_length = 50)
    class Meta:
        db_table = 'student'

class Universities(models.Model):
    uni_id = models.IntegerField(db_column='id')
    name = models.CharField(db_column = 'name',max_length = 75,primary_key=True)
    class Meta:
        db_table = 'university'

class messenger(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(db_column = 'sender',max_length = 75)
    reciever = models.CharField(db_column='reciever',max_length=75)
    fileurl = models.CharField(db_column='fileurl', max_length=500)
    dated = models.DateField(db_column='date')
    time = models.TimeField(db_column='time')
    status = models.IntegerField(db_column='status')
    remarks = models.CharField(db_column='remarks',max_length=150)
    nameStudent = models.CharField(db_column= 'stuname',max_length=50)
    #id = models.IntegerField(db_column='id',primary_key=True)
    class Meta:
        db_table = 'messages'

class course (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='name',max_length=50)
    code = models.CharField(db_column='code',max_length=10)

    class Meta:
        db_table = 'course'

class semester (models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(db_column='year')
    type = models.CharField(db_column='type',max_length=10)
    number = models.IntegerField(db_column='number')

    class Meta:
        db_table = 'semester'

class semester_course_mapping (models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.IntegerField(db_column='course_id')
    semester_id = models.IntegerField(db_column='semester_id')

    class Meta:
        db_table = 'semester_course_mapping'


class student_course_mapping (models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(db_column='student_id')
    semester_course_mapping_id = models.IntegerField(db_column='semester_course_mapping_id')
    grade = models.CharField(db_column='grade',max_length=2, null=True)
    class Meta:
        db_table = 'student_course_mapping'


class student_semester_mapping (models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.IntegerField(db_column='student_id')
    semester_id = models.IntegerField(db_column='semester_id')
    spi = models.FloatField(db_column='spi', null = True)
    class Meta:
        db_table = 'student_semester_mapping'

class faculty_course_mapping (models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.IntegerField(db_column='faculty_id')
    semester_course_mapping_id = models.IntegerField(db_column='semester_course_mapping_id')

    class Meta:
        db_table = 'faculty_course_mapping'
# Create your models here.
