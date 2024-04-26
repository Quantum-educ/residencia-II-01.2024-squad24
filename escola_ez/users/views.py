from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, StudentSignInForm


def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, 'users.backends.EmailBackend')
            return redirect('/user')
        return render(request, 'signup.html', {'form': form})
    else:
        form = StudentSignUpForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = StudentSignInForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            login(request, user, 'users.backends.EmailBackend')
            return redirect('/user')
        return render(request, 'signin.html', {'form': form})
    else:
        form = StudentSignInForm()

    return render(request, 'signin.html', {'form': form})


@login_required
def userpage(request):
    return render(request, 'userpage.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def assessment(request):
    return render(request, 'assessment.html')
