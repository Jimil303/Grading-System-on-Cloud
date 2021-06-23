from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from grading.models import FacultyCredentials
from grading.models import StudentCredentials
from .forms import Myform
import csv
import os

def login(request):
    return render(request,'login.html')

def loginstudent(request):
    return render(request,'loginpagestudent.html')

def loginfaculty(request):
    return render(request,'loginpagefaculty.html')

def loginadmin(request):
    return render(request,'loginpageadmin.html')

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
                created = StudentCredentials.objects. get_or_create(
                    username = row[0],
                    password = row[1],
                    auth = False,
                    university = row[2],
                )
                try:
                    created.save()
                except:
                    continue
        context = {'filePathName': filePathName}
    return render(request, 'RegisterUsers.html', context)
    

    

def search(request):
    return render(request,'Search.html')

def notification(request):
    return render(request,'Notification.html')

def sendreq(request):
    return render(request,'StudentValidation.html')

#def userreg(request):




# Create your views here
