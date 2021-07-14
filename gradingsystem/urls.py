"""gradingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from grading import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage.html',views.index, name = 'home'),
    path('login.html', views.login, name='login'),
    url('loginstudent', views.studenthomepage, name='homepage'),
    url('loginpagestudent', views.loginstudent, name='loginstudent'),
    url('loginpagefaculty', views.loginfaculty, name='loginpagefaculty'),
    url('loginadmin', views.loginadmin, name='loginadmin'),
    url('RegisterUsersfaculty',views.reguser1,name='RegisterUsersfaculty'),
    url('reguser2',views.reguser2,name='RegisterUsers'),
    url('RegisterUsersstudent',views.reguser3,name='RegisterUsersstudent'),
    url('reguser4',views.reguser4,name='RegisterUsers'),
    url('Search',views.search,name='Search'),
    url('notifications-recieved',views.notification_recieved,name = 'Notification'),
    url('notifications-pending',views.notification_pending,name = 'Notification'),
    url('notifications-sent',views.notification_sent,name = 'Notification'),
    url('StudentValidation',views.StudentValidation,name='StudentValidation'),
    url('studenthomepage',views.studenthomepage,name='studenthomepage'),
    url('result',views.result,name='result'),
    url('loginfaculty',views.loginfaculty,name  = 'loginfaculty'),
    url('selectsemester2',views.selectsem2,name = 'selectsemester2'),
    url('selectsem2',views.selectsem2,name = 'selectsemester2'),
    url('selectsemester',views.selectsem,name = 'selectsemester'),
    url('selectsem',views.selectsem,name = 'selectsemester'),
    url('courseregistration',views.coursereg,name='courseregistration'),
    url('coursereg',views.coursereg,name='courseregistration'),
    url('shownames',views.shownames,name='shownames'),
    url('updateprofilestudent',views.updateprofilestudent,name='updateprofile'),
    url('transcript',views.transcript,name='transcript'),
    url('addcourses',views.addonecourse,name = 'Addonecourse'),
    url('addmanycourses',views.addmanycourses,name = 'Addmanycourses'),
    url('addsemester',views.addsemester,name = 'Addsemester'),
    url('semcoursemapping',views.semcoursemapping,name = 'semcoursemapping'),
    url('facultyhomepage',views.facultyhomepage,name='facultyhomepage'),
    url('facultycourses',views.facultycourses,name = 'facultycourses'),
    url('selectcourse',views.selectcourse,name = 'selectcourse'),
    url('uploadgrades',views.uploadgrades,name = 'uploadgrades'),
    
    url('updateprofilefaculty',views.updateprofilefaculty,name = 'updateprofilefaculty'),
    url('getstudentlist.html',views.getstudentlist,name = 'getstudentlist'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
