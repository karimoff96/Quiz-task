from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'app/home.html', {})

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=email)
        if user is None:
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = fname
            new_user.last_name = lname
            new_user.save()
            return redirect('login-page')
        else:
            messages.error(request,"This email is already in use, please try another one")
            return redirect('register-page')
    return render(request, 'app/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')           
        else:
            messages.error(request,"Invalid login credentials")
            return redirect('login-page')
    return render(request, 'app/login.html')


def log_out(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'app/test.html')