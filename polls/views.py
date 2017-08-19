from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import  forms
from .forms import UserRegistrationForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World. You are the polls index")

def home(request):
    render(request, 'app/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            last_name = userObj['last_name']
            first_name = userObj['first_name']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = User.objects.create_user(username, email, password)
                user.last_name = last_name
                user.first_name = first_name
                user.save()
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/polls/profile/')
            else:
                raise forms.ValidationError("Oops! Something went wrong. Username or email already exist")

    else:
        form = UserRegistrationForm
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request, 'profile/index.html', {'user': user})
    else:
        return


def edit_profile(request): 
    if request.user.is_authenticated():
        user = request.user
        return render(request, 'profile/edit.html', {'user': user})
    else:
        return   