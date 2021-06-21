from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from grading.models import FacultyCredentials
from grading.models import StudentCredentials
from .forms import Myform
import csv
import os



def index(request):
    return render(request,'homepage.html')

def reguser(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = Myform()
    return render(request, 'regUser.html', {'form' : form})

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
    return render(request, 'regUser.html', context)
    

    

def search(request):
    return render(request,'search.html')

def notification(request):
    return render(request,'notifications.html')

def sendreq(request):
    return render(request,'sendReq.html')

#def userreg(request):




# Create your views here
