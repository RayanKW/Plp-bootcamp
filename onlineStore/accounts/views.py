from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerSignUpForm

# Create your views here.


def login(request):
    pass


def register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(Name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = CustomerSignUpForm()
    return render(request, 'registration/register.html', {'form':form})
