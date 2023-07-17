from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
#from .models import Record


# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,"home.html")


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user :
            login(request,user)
            messages.success(request,"You have been loged In")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return render(request,"login.html")
    return render(request,"login.html")


def user_logout(request):
    logout(request)
    return redirect('login')

def user_signUp(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form =SignUpForm()
        
    return render(request,'register.html',{'form':form})