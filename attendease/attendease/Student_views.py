from django.shortcuts import render,redirect
from app.EmailBackEnd import EmailBackEnd
from app.models import CustomUser
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def HOME(request):
    return render(request,'Student/Student_home.html')
