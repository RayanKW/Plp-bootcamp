from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def About(request):
    return render(request,'home/about.html')