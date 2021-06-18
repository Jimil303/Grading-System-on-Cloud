from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage



def index(request):
    return render(request,'homepage.html')

def reguser(request):
    return render(request,'regUser.html')


# Create your views here
