from django.shortcuts import render

# Create your views here.
# from django.shortcuts import  render,redirect,HttpResponse
# from datetime import datetime
# from home.models import Contact,Mhtcetregister,Slotbook
# from django.contrib.auth import authenticate,logout,login
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from home.middlewares import guest , auth



# Create your views here.\
# @login_required(login_url='loginuser')
def index(request):
    return render(request,'index.html')



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

def student_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return render(request,'index.html')
    return render(request,'student_login.html')
