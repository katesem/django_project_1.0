from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm
from .models import Users
from django.contrib import messages
from django.contrib.auth import  logout, authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

Users = get_user_model()


def homepage(request):
    return render(request, 'homepage.html')

def about_page(request):
    return render(request, 'about.html' )

@login_required
def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = Users.create(form.cleaned_data['email'], form.cleaned_data['username'], form.cleaned_data['password'])
            new_user = authenticate(username=user.username, password = user.password)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome to site, {user.username}")
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'log_in.html', {'form': form})


'''
def user_form(request, user_id = 0):
    if request.method == "GET":
        if user_id == 0:
            form = UserForm()
        else:
            user = get_object_or_404(CustomUser, pk = user_id)
            form = UserForm(instance = user)
        return render(request, 'user_form.html', {'form': form})
    else:
        if user_id == 0:
            form = UserForm(request.POST)
            if form.is_valid():
                new_user = CustomUser.create(**form.cleaned_data).save()
            else:
                form = UserForm()
        else:
            user = get_object_or_404(CustomUser, pk = user_id)
            form = UserForm(request.POST, instance = user)
            if form.is_valid():
                user.update(form.cleaned_data['first_name'], 
                            form.cleaned_data['last_name'],
                            form.cleaned_data['middle_name'],
                            form.cleaned_data['password'] )
            
            else:
                form = UserForm()
'''