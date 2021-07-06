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
    path('', views.login, name='login'),
    url('loginpagestudent', views.loginstudent, name='loginpagestudent'),
    url('loginpagefaculty', views.loginfaculty, name='loginpagefaculty'),
    url('loginadmin', views.loginadmin, name='loginadmin'),
    url('RegisterUsersfaculty',views.reguser1,name='RegisterUsers'),
    url('reguser2',views.reguser2,name='RegisterUsers'),
    url('RegisterUsersstudent',views.reguser3,name='RegisterUsers'),
    url('reguser4',views.reguser4,name='RegisterUsers'),
    url('Search',views.search,name='Search'),
    url('Notification',views.notification,name='Notification'),
    url('StudentValidation',views.StudentValidation,name='StudentValidation'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
