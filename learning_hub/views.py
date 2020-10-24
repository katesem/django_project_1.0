from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, QuestionForm
from .models import Users
from django.contrib import messages
from django.contrib.auth import  logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django import forms

Users = get_user_model()


def homepage(request):
    return render(request, 'homepage.html')


def about_page(request):
    return render(request, 'about.html' )


def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = Users.create(form.cleaned_data['email'], form.cleaned_data['username'], form.cleaned_data['password'])
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['Username'], password = form.cleaned_data['Password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'log_in.html', {'form':  LoginForm(), 'u_error':'Your entered wrong data. Check your input and repeat log in.'})

    return render(request, 'log_in.html', {'form':  LoginForm()})

def log_out(request):
    logout(request)
    return redirect('/')


def my_account(request):
    return render(request, 'my_account.html')

    
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_account')
    return render(request, 'c_question.html', {'form' : QuestionForm()})

def password_redirect(request):
    return redirect('/log_in')
