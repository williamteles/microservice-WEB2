from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'web/index.html', {})

def login(request):
    return render(request,'register/login.html',{})

def register_user(request):
    # form = UserForm()
    return render(request,'register/register_user.html',{})

def register_account(request):
    return render(request,'register/register_account.html',{})

def home(request):
    return render(request,'web/home.html',{})