from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Hiretuber

def hiretubers(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        tuber_id=request.POST['tuber_id']
        email=request.POST['email']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']
        hiretuber=Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,email=email,tuber_name=tuber_name,city=city,state=state,phone=phone,message=message,user_id=user_id)
        print(hiretuber)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('youtubers')