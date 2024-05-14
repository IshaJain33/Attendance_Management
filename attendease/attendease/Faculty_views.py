from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Branch,Faculty,Coordinator,Department,Student,Session_Year,Subject
from app.models import CustomUser
from django.contrib import messages


def HOME(request):
    return render(request,'Faculty/Faculty_home.html')


def FACULTY_TAKE_ATTENDANCE(request):
    faculty_id = Faculty.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(faculty=faculty_id)

    context = {
        'subject' : subject
    }
    return render(request,'Faculty/faculty_take_attendance.html',context)