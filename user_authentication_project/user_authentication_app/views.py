from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import HttpResponseRedirect, render

from .forms import CustomSignupForm, UpdateUserProfileForm


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'account/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('login')


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateUserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = UpdateUserProfileForm(instance=request.user)
        return render(request, 'account/profile_update.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


def change_user_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect('/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'account/change_password.html', {'form': form})
    else:
        return HttpResponseRedirect('login')
