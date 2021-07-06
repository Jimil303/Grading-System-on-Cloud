from django.contrib.auth.models import UserManager
from django.core.checks import messages
from django.core.files.base import File
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from grading.models import FacultyCredentials, admin ,messenger, StudentCredentials
from .forms import Myform , Myform2
from datetime import datetime
import csv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import ipdb

def login(request):

    return render(request,'login.html')

def loginstudent(request):
    
    return render(request,'loginpagestudent.html',)

def loginfaculty(request):
    return render(request,'loginpagefaculty.html')


def loginadmin(request):
    if request.method == 'POST':
        m = admin.objects.get(username = request.POST['username'])
        if m.password == request.POST['password']:
            request.session['college'] = m.university
            #print(sess['college'])
            return render(request, 'homepage.html')
        else:
            return render(request,'loginadmin.html')
    return render(request,'loginadmin.html')

def index(request):
    return render(request,'homepage.html')

def reguser1(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        form_class = Myform
        if form.is_valid():
            form.save()
    else:
            form = Myform()
    return render(request, 'RegisterUsersfaculty.html', {'form' : form})

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
                created = FacultyCredentials.objects.get_or_create(
                    name = row[0],
                    phone = row[1],
                    email = row[2],
                    username = row[3],
                    password = row[4],
                )
                try:
                    created.save()
                except:
                    continue
        context = {'filePathName': filePathName,}
    return render(request, 'RegisterUsersfaculty.html', context)
    
def reguser3(request):
    if request.method == 'POST':
        form = Myform2(request.POST)
        form_class = Myform2
        if form.is_valid():
            form.save()
    else:
            form = Myform2()
    return render(request, 'RegisterUsersstudent.html', {'form' : form})

def reguser4(request):
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
                    name = row[0],
                    phone = row[1],
                    email = row[2],
                    username = row[3],
                    password = row[4],
                )
                try:
                    created.save()
                except:
                    continue
        context = {'filePathName': filePathName,}
    return render(request, 'RegisterUsersstudent.html', context)
    
def search(request):
    return render(request,'Search.html')

def notification(request):
    user = request.session['college']
    
    details = messenger.objects.filter(reciever = user,status = False).all()
    
    print(details[0].date)  
    print(user)
    
    return render(request,'Notification.html')

def StudentValidation(request):
    if request.method == 'POST':
        form_class = Myform
        fileobj = request.FILES['pdffile']
        fs = FileSystemStorage()
        filepathname = fs.save(fileobj.name,fileobj)
        #uploaded_to = fs.path(filepathname)
        upload_data = cloudinary.uploader.upload(filepathname).get('secure_url')
        name = request.POST['name']
        send_to = request.POST['search']
        now = datetime.now()
        datee = now.strftime("%Y-%m-%d")
        timee = now.strftime("%H:%M:%S")
        print(upload_data)
        print(name)
        print(send_to)
        #print(sess["college"])
        created = messenger.objects.get_or_create(
            reciever = send_to,
            fileurl = upload_data,
            dated = datee,
            time = timee,
            status = 0,
            remarks = "",
            nameStudent = name,
            sender = request.session['college'],
            
        )
        try:
            created.save()
        except:
            return render (request,'StudentValidation.html', )
    return render(request,'StudentValidation.html',)

#def userreg(request):




# Create your views here
