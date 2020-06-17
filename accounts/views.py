from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("user is valid")
            return redirect(reverse('recipes:index'))
        else:
            print("oops")
            messages.info(request, "username and/or password incorrect")

    context = {}
    return render(request, 'login.html', context)


def register_view(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('accounts:login'))

    context = {'form': form}
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:login'))
