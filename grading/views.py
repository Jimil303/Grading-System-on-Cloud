from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage



def index(request):
    return render(request,'HomePage.html')

def reguser(request):
    return render(request,'RegisterUsers.html')

def search(request):
    return render(request,'Search.html')

def notification(request):
    return render(request,'Notification.html')

def sendreq(request):
    return render(request,'StudentValidation.html')

    



# Create your views here
