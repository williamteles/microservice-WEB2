from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/index.html', {})

def login(request):
    return render(request,'register/login.html',{})

def register_user(request):
    return render(request,'register/register_user.html',{})