from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def welcome(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        log = request.POST.get('email')
        passw = request.POST.get('pass')
        user = authenticate(username=log, password=passw)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def hello(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    else:
        return redirect('/login/')

def add_student(request):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        Student.objects.create(name=a, age=b, level=c, student_int=d)

        return redirect("/student/")

    return render(request, 'add_student.html')


def students(request):
    data = {
        'Student': Student.objects.all()
    }
    return render(request, 'students.html', data)


def delete_student(request, a):
    Student.objects.get(id=a).delete()
    return redirect('/student/')


def delete_plan(request, id):
    Plan.objects.get(id=id).delete()
    return redirect('/plans/')


def student_update(request, id):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        Student.objects.filter(id=id).update(name=a, age=b, level=c, student_int=d)
        return redirect('/student/')
    return render(request, 'student_edit.html')


def plan_update(request, id):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        Plan.objects.filter(id=id).update(title=a, description=b, status=c, student=d)
        return redirect('/plans/')
    return render(request, 'plan_edit.html')


def plan_up_data(request, id):
    data = {
        'plan': Plan.objects.get(id=id),
        'Student': Student.objects.all()
    }
    return render(request, 'plan_edit.html', data)


def plan_add_data(request):
    data = {
        'Student': Student.objects.all()
    }
    return render(request, 'add_plan.html', data)


def student_up_data(request, a):
    data = {
        'student': Student.objects.get(id=a)
    }
    return render(request, 'student_edit.html', data)


def add_plan(request):
    if request.method == "POST":
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        d = request.POST.get('d')
        e = Student.objects.get(id=d)
        Plan.objects.create(title=a, description=b, status=c, student=e)
        return redirect('/plans/')
    return render(request, 'add_plan.html')


def plan(request):
    data = {
        'students': Student.objects.all(),
        'Plans': Plan.objects.all(),
    }
    return render(request, 'plans.html', data)
