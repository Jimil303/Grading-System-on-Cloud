from django.core.files.base import File
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from grading.models import FacultyCredentials, Universities,messenger
from grading.models import StudentCredentials
from .forms import Myform
from datetime import datetime
import csv
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

def login(request):

    return render(request,'login.html')

def loginstudent(request):
    
    return render(request,'loginpagestudent.html',)

def loginfaculty(request):
    return render(request,'loginpagefaculty.html')


def loginadmin(request):
    if request.method == 'POST':
        u1 = request.POST['username']
        p1 = request.POST['password']
        #query = 'select * from university where username = %s and password = %s' [u1],[p1]
        try:
            details = Universities.objects.filter(username = u1 , password = p1).get()
        except:
            return render(request,'loginadmin.html')

        if details != NullBooleanField:
            context = {'name' : details.name , 'username' : details.username}
            return render (request, 'homepage.html',context)

    return render(request,'loginadmin.html')

def index(request):
    return render(request,'homepage.html')

def reguser(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = Myform()
    return render(request, 'RegisterUsers.html', {'form' : form})

def reguser2(request):
    if request.method == 'POST':
        fileobj = request.FILES['csvfile']
        fs = FileSystemStorage()
        filePathName = fs.save(fileobj.name, fileobj)
        #filePathName = fs.url(filePathName)
        uploaded_to = fs.path(filePathName)
        print(uploaded_to)
        with open(uploaded_to) as f:
            reader = csv.reader(f)
            for row in reader:
                created = StudentCredentials.objects.get_or_create(
                    username = row[0],
                    password = row[1],
                    auth = False,
                    university = row[2],
                )
                try:
                    created.save()
                except:
                    continue
        context = {'filePathName': filePathName,}
    return render(request, 'RegisterUsers.html', context)
    

    

def search(request):
    return render(request,'Search.html')

def notification(request):
    return render(request,'Notification.html')

def StudentValidation(request):
    if request.method == 'POST':
        fileobj = request.FILES['pdffile']
        fs = FileSystemStorage()
        filepathname = fs.save(fileobj.name,fileobj)
        #uploaded_to = fs.path(filepathname)
        upload_data = cloudinary.uploader.upload(filepathname)
        name = 'shabbir'
        send_to = 'New York University'
        now = datetime.now()
        datee = now.strftime("%Y-%m-%d")
        timee = now.strftime("%H:%M:%S")
        print(upload_data[17])
        print(name)
        print(send_to)
        created = messenger.objects.get_or_create(
            reciever = send_to,
            fileurl = upload_data[17],
            dated = datee,
            time = timee,
            status = False,
            remarks = "NIL",
            nameStudent = name,
            sender = "Dhirubhai Ambani Institute of Information and Communcation Technology",
        )
        try:
            created.save()
        except:
            return render (request,'StudentValidation.html', )
    return render(request,'StudentValidation.html',)

#def userreg(request):




# Create your views here
