from django.shortcuts import render


# Create your views here.
from kanban_life.home.models import User


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def sign_up(request):
    if request.POST:
        nome_completo = request.POST['nome_completo']
        email = request.POST['email']
        senha = request.POST['senha']
        user = User()
        user.password = senha
        user.email = email
        user.first_name = nome_completo
        user.save()

    return render(request, 'home/sign_up.html')
