from django.shortcuts import render
from Users.forms import StudentForm, StudentComplains, TeacherFeedback, TeacherComplains, RegisterForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def teachers(request):
    form = RegisterForm()  # empty form
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # whatever typed is saved in this form
        if form.is_valid():
            form.save()
    else:  # if not post, then just give an empty form
        form = RegisterForm()
    return render(request, 'teachers.html', {'form': form})


def students(request):
    return render(request, 'students.html')


def contact(request):
    return render(request, 'contact.html')


def stud_signup(request):
    return render(request, 'StudentSignUp.html')


def stud_login(request):
    return render(request, 'StudentLogin.html')


def teacher_signup(request):
    form = TeacherComplains
    return render(request, 'TeacherSignUp.html', {'form': form})


def teacher_login(request):
    form = TeacherFeedback
    return render(request, 'TeacherLogin.html', {'form': form})


def student_signup(request):
    form = StudentForm
    return render(request, 'StudentSignUp.html', {'form': form})


def student_login(request):
    form = StudentComplains
    return render(request, 'StudentLogin.html', {'form': form})
