from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.conf import settings


# Create your views here.


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(response, "registration/register.html", {"form": form})


def logout_done(response):
    return render(response, "registration/logout_done.html")


def login_done(response):
    return render(response, "registration/login_done.html")
