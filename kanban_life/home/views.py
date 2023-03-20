import json

from django.http import HttpResponse
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

        retorno = {
            'STATUS': 'OK',
            'mensagem': 'Conta Criada!'
        }
        return HttpResponse(json.dumps(retorno), content_type='application/json')

    return render(request, 'home/sign_up.html')


def verificar_email_ja_existente(request):  # Vai verificar se já tem algum usuario com o email que vai ser passado
    existe = False
    email = request.POST['email_verificar']
    users = User.objects.filter(email=email)
    if users:
        existe = True

    retorno = {
        'STATUS': 'OK',
        'existe': existe
    }

    return HttpResponse(json.dumps(retorno), content_type='application/json')