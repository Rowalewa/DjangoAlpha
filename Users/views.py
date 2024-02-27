from django.shortcuts import render
from Users.forms import StudentForm, StudentComplains, TeacherFeedback


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


def stud_signup(request):
    return render(request, 'StudentSignUp.html')


def stud_login(request):
    return render(request, 'StudentLogin.html')


def teacher_signup(request):
    return render(request, 'TeacherSignUp.html')


def teacher_login(request):
    form = TeacherFeedback
    return render(request, 'TeacherLogin.html', {'form': form})


def student_signup(request):
    form = StudentForm
    return render(request, 'StudentSignUp.html', {'form': form})


def student_login(request):
    form = StudentComplains
    return render(request, 'StudentLogin.html', {'form': form})
