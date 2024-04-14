from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import StudentForm


def signup(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = StudentForm()

    return render(request, "signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = StudentForm()

    return render(request, "signin.html", {"form": form})
