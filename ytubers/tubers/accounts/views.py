from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if len(password) >= 8 and len(password) <=16:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username already exists!")
                    print("Username already exists!")
                    return redirect("register")
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'Email already exists!')
                        print("Email already exists!")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(first_name=firstname, last_name = lastname,username=username,email=email,password=password)
                        user.save()
                        messages.success(request,"Account created successfully!!")
                        print("Account created successfully!!")
                        return redirect('login')
            else:
                messages.error(request,"Passwords do not match")
                print("Passwords do not match")
                return redirect('login')
        else:
            messages.warning(request,"Password length should be between 8-16")
            print("Password length should be between 8-16")
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in successfully")
            print("Logged in successfully")

        else:
            messages.warning(request,"Invalid credentials")
            print("Invalid credentials")
            return redirect("login")
    return render(request, 'accounts/login.html')
    

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')