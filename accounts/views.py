# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
# from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, ProfileUpdateForm 

def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # The profile is created automatically via signals
            login(request, user)
            return redirect('home')
    else:
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def update_profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'accounts/update_profile.html', {'form': form})