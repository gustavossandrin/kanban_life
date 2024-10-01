from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from kanban_life.login.forms import LoginForm


def login_index(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/board/' + str(user.id))
        else:
            return render(request, 'login/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


def login_exit(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_index'))
