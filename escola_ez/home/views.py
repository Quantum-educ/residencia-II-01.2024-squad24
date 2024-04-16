from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('/user')
    return render(request, 'index.html')
