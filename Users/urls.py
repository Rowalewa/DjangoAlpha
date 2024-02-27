"""
URL configuration for OnlineExaminationSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('contact/', views.contact, name='contact'),
    path('StudentSignUp/', views.student_signup, name='stud_signup'),
    path('StudentLogin/', views.student_login, name='stud_login'),
    path('TeacherLogIn/', views.teacher_login, name='teacher_login'),
    path('TeacherSignUp/', views.teacher_signup, name='teacher_signup')
]
