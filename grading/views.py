from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage



def index(request):
    return render(request,'homepage.html')

def reguser(request):
    return render(request,'regUser.html')

def search(request):
    return render(request,'search.html')

def notification(request):
    return render(request,'notifications.html')

def sendreq(request):
    return render(request,'sendReq.html')

    



# Create your views here
