from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import SignUpForm, LogInForm

def home_page_view(request):
    return HttpResponse("Welcome to Clean Social Network! 👋")


def welcome(request):
    # Assuming the user is already authenticated
    User = get_user_model()
    if request.user.is_authenticated:
        username = request.user.username
        user_score = request.user.score  # Retrieve the user's score
        return render(request, 'welcome.html', {'username': username, 'score': user_score})
    else:
        # Handle the case when the user is not authenticated
        return render(request, 'not_authenticated.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LogInForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('welcome')  # Redirect to your home page
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})
