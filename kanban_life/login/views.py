from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from kanban_life.login.forms import LoginForm


def login_index(request):
    msg_aviso = ""
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()

            if user.is_superuser:
                request.session['tipo_usuario'] = "superuser"
            else:
                request.session['tipo_usuario'] = "user"

            login(request, user)
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'login/login.html')