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

# Create your models here.
