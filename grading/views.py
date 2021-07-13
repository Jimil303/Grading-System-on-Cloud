from django.contrib.auth.models import UserManager
from django.core.checks import messages
from django.core.files.base import File
from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.utils.functional import empty
from grading.models import FacultyCredentials, admin, course, faculty_course_mapping ,messenger, StudentCredentials,semester, semester_course_mapping, student_course_mapping
from .forms import Myform , Myform2, Myform3, Myform4
from datetime import datetime
import csv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import ipdb

def login(request):

    return render(request,'login.html')

def loginstudent(request):
    if request.method == 'POST':
        m = StudentCredentials.objects.get(username = request.POST['username'])
        if m.password == request.POST['password']:
            request.session['student_id'] = m.stu_id
            return render(request, 'studenthomepage.html')
        else:
            return render(request,'loginpagestudent.html')
    return render(request,'loginpagestudent.html')

def loginfaculty(request):
    if request.method == 'POST':
        m = FacultyCredentials.objects.get(username = request.POST['username'])
        
        if m.password == request.POST['password']:
            
            request.session['faculty_id'] = m.fac_id
            return render(request, 'facultyhomepage.html')
        else:
            return render(request,'loginpagefaculty.html')
    return render(request,'loginpagefaculty.html')


def loginadmin(request):
    if request.method == 'POST':
        m=admin.objects.get(username = request.POST['username'])
        if m.password == request.POST['password']:
            request.session['college'] = m.university
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
                    fac_id =row[0],
                    name = row[1],
                    phone = row[2],
                    email = row[3],
                    username = row[4],
                    password = row[5],
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
                created=StudentCredentials.objects.get_or_create(
                    stu_id =row[0],
                    name = row[1],
                    phone = row[2],
                    email = row[3],
                    username = row[4],
                    password = row[5],
                )
                try:
                    created.save()
                except:
                    continue
        context = {'filePathName': filePathName,}
    return render(request, 'RegisterUsersstudent.html', context)
    
def search(request):
    return render(request,'Search.html')

def notification_recieved(request):
    user = request.session['college']
    
    details = messenger.objects.filter(reciever = user).order_by('dated').all()
    print(details)
    return render(request,'notifications-recieved.html',{'det' : details})

def notification_pending(request):
    user = request.session['college']
    
    details = messenger.objects.filter(reciever = user,status = 0).order_by('dated').all()
    print(details)
    return render(request,'notifications-pending.html',{'det' : details})

def notification_sent(request):
    user = request.session['college']
    
    details = messenger.objects.filter(sender = user).order_by('dated').all()
    print(details)
    return render(request,'notifications-sent.html',{'det' : details})

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
        created=messenger.objects.get_or_create(
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

def studenthomepage(request):

    return render(request,'studenthomepage.html')


def coursereg(request):
    if request.method == 'POST':
        stu_id = request.session['student_id']
        print(request.session['sem'])
        print(stu_id)
        #print(request.session['year'])
        semid = semester.objects.get(year = request.session['year'],number = request.session['sem'])
        if request.POST.get('course1'):
            cr1 = course.objects.get(code = request.POST['course1'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            )
        if request.POST.get('course2'):
            cr1 = course.objects.get(code = request.POST['course2'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            ) 
        if request.POST.get('course3'):
            cr1 = course.objects.get(code = request.POST['course3'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            )
        if request.POST.get('course4'):
            cr1 = course.objects.get(code = request.POST['course4'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            ) 
        if request.POST.get('course5'):
            cr1 = course.objects.get(code = request.POST['course5'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            )
        if request.POST.get('course6'):
            cr1 = course.objects.get(code = request.POST['course6'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            student_course_mapping.objects.get_or_create(
                student_id = stu_id,
                semester_course_mapping_id = sem_cr_mp.id
            ) 
    return render(request,'courseregistration.html')

def selectsem(request):
    
    if request.method == 'POST':
        if request.POST['sem'] == "Semester I":
            request.session['sem'] = 1
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester II":
            request.session['sem'] = 2
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester III":
            request.session['sem'] = 3
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester IV":
            request.session['sem'] = 4
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester V":
            request.session['sem'] = 5
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VI":
            request.session['sem'] = 6
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VII":
            request.session['sem'] = 7
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VIII":
            request.session['sem'] = 8
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'courseregistration.html',{'shownames' : results})
        else:
            return render(request,'selectsemester.html')
    return render(request,'selectsemester.html')

def updateprofilestudent(request):

    return render(request,'updateprofilestudent.html')


def result(request):

    return render(request,'result.html')

def transcript(request):
    
    return render(request,'transcript.html')

def addmanycourses(request):
    if request.method == 'POST':
        fileobj = request.FILES['csvfile']
        fs = FileSystemStorage()
        filePathName = fs.save(fileobj.name, fileobj)
        uploaded_to = fs.path(filePathName)
        print(uploaded_to)
        with open(uploaded_to) as f:
            reader = csv.reader(f)
            for row in reader:
                created = course.objects.get_or_create(
                    name = row[0],
                    code = row[1],
                )
                try:
                    created.save()
                except:
                    continue
    return render(request,'addcourses.html')
def addmanycourses(request):
    if request.method == 'POST':
        fileobj = request.FILES['csvfile']
        fs = FileSystemStorage()
        filePathName = fs.save(fileobj.name, fileobj)
        uploaded_to = fs.path(filePathName)
        print(uploaded_to)
        with open(uploaded_to) as f:
            reader = csv.reader(f)
            for row in reader:
                created = course.objects.get_or_create(
                    name = row[0],
                    code = row[1],
                    credits = row[2],
                    kind = row[3],
                )
                try:
                    created.save()
                except:
                    continue
    return render(request,'addcourses.html')

def addonecourse(request):
    if request.method == 'POST':
        form = Myform3(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = Myform3()
    return render(request,'addcourses.html',{'form' : form})

def addsemester(request):
    if request.method =='POST':
        form = Myform4(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = Myform4()
    return render(request,'addsemester.html',{'form' : form})

def semcoursemapping(request):
    courses = shownames(request)
    if request.method == 'POST':
        
        semno = request.POST['semno']
        years = request.POST['Year']
        print(semno)
        print(years)
        semid = semester.objects.get(year = years,number = semno)
        print(semid)
        if request.POST['course1']:
            cr1 = course.objects.get(code = request.POST['course1'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr1.id
            )
            
        if request.POST['course2']:
            cr2 = course.objects.get(code = request.POST['course2'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr2.id
            )
            
        if request.POST['course3']:
            cr3 = course.objects.get(code = request.POST['course3'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr3.id
            )
            
        if request.POST['course4']:
            cr4 = course.objects.get(code = request.POST['course4'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr4.id
            )
            
        if request.POST['course5']:
            cr5 = course.objects.get(code = request.POST['course5'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr5.id
            )
            
        if request.POST['course6']:
            cr6 = course.objects.get(code = request.POST['course6'])
            semester_course_mapping.objects.get_or_create(
                semester_id = semid.id,
                course_id = cr6.id
            )
                
        
    return render(request,'semcoursemapping.html',{'shownames':courses})

def shownames(request):
    results=course.objects.all()
    return results

def facultyhomepage(request):

    return render(request,'facultyhomepage.html')


def grades(request):
    
    return render(request,'grades.html')

def displaycourse(sem, yr):
    x = semester.objects.get(year = yr, number = sem)
    y = semester_course_mapping.objects.filter(semester_id = x.id).all()
    print(y[0].id)
    list =[]
    for i in y:
        list.append(course.objects.get(id = i.course_id))
    return list

def selectsem2(request):
    if request.method == 'POST':
        if request.POST['sem'] == "Semester I":
            request.session['sem'] = 1
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester II":
            request.session['sem'] = 2
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester III":
            request.session['sem'] = 3
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester IV":
            request.session['sem'] = 4
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester V":
            request.session['sem'] = 5
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VI":
            request.session['sem'] = 6
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VII":
            request.session['sem'] = 7
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        elif request.POST['sem'] == "Semester VIII":
            request.session['sem'] = 8
            request.session['year'] = request.POST['year']
            results = displaycourse(request.session['sem'],request.session['year'])
            return render(request,'facultycourses.html',{'shownames' : results})
        else:
            return render(request,'selectsem2.html')
    return render(request,'selectsem2.html')

def facultycourses(request):
    if request.method == 'POST':
        fac_id = request.session['faculty_id']
        print(request.session['sem'])
        print(fac_id)
        
        semid = semester.objects.get(year = request.session['year'],number = request.session['sem'])
        if request.POST.get('course1'):
            cr1 = course.objects.get(code = request.POST['course1'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            faculty_course_mapping.objects.get_or_create(
                faculty_id = fac_id,
                semester_course_mapping_id = sem_cr_mp.id
            )
        if request.POST.get('course2'):
            cr1 = course.objects.get(code = request.POST['course2'])
            sem_cr_mp = semester_course_mapping.objects.get(semester_id = semid.id, course_id = cr1.id)
            faculty_course_mapping.objects.get_or_create(
                faculty_id = fac_id,
                semester_course_mapping_id = sem_cr_mp.id
            ) 
    return render(request,'facultycourses.html')

def updateprofilefaculty(request):

    return render(request,'updateprofilefaculty.html')

def get_courses(request):
    x = faculty_course_mapping.objects.filter(faculty_id = request.session['faculty_id']).all()
    temp = []
    for i in x:
        temp.append(semester_course_mapping.objects.get(id = i.semester_course_mapping_id))
    lis = []
    for t in temp:
        lis.append(course.objects.get(id = t.course_id))
    return lis

def selectcourse(request):
    x = get_courses(request)
    if request.method == 'POST':
        request.session['course_selec'] = request.POST['course1']
        return render (request,'uploadgrades.html')
    return render(request,'selectcourse.html',{'shownames' : x})
def uploadgrades(request):
    
    return render(request,'uploadgrades.html')

def editgrades(request):
    
    return render(request,'editgrades.html')