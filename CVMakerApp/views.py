from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request, type):
    return render(request, 'create.html')