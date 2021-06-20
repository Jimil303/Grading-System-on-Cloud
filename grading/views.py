from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from grading.models import FacultyCredentials
from .forms import Myform



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

def search(request):
    return render(request,'search.html')

def notification(request):
    return render(request,'notifications.html')

def sendreq(request):
    return render(request,'sendReq.html')

#def userreg(request):




# Create your views here
