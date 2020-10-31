from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, QuestionSingleOrderForm, QuizCreationForm
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
        form = QuestionSingleOrderForm(request.POST)

        if form.is_valid():
            if form.instance.answer == '1':                    # it's not an example of good code 
                form.instance.answer = form.instance.option1
            elif form.instance.answer == '2':
                form.instance.answer = form.instance.option2
            elif form.instance.answer == '3':
                form.instance.answer = form.instance.option3
            else:
                form.instance.answer == form.instance.option4
            form.save()
            return redirect('/my_account')
    return render(request, 'c_question.html', {'form' : QuestionSingleOrderForm()})


def create_quiz(request):
    if request.method == "POST":
        form = QuizCreationForm(request.POST)
    return render(request, 'c_quiz.html', {'form': QuizCreationForm})
    
    
def password_redirect(request):
    return redirect('/log_in')
