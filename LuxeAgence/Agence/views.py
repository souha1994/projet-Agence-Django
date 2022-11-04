from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def apropos(request):
    return render(request,'apropos.html')
def contacteznous(request):
    return render(request,'contacteznous.html')