from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def teachers(request):
    return render(request, 'teachers.html')


def students(request):
    return render(request, 'students.html')


def contact(request):
    return render(request, 'contact.html')


def admins(request):
    return render(request, 'admins.html')