import json
from django.http import HttpResponse
from django.shortcuts import render
from kanban_life.home.models import User
from kanban_life.tools.views import criar_colunas_iniciais


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def sign_up(request):
    if request.POST:
        nome_completo = request.POST['nome_completo']
        email = request.POST['email']
        senha = request.POST['senha']

        user = User.objects.create_user(email, senha, first_name=nome_completo)
        user.save()

        retorno = {
            'STATUS': 'OK',
            'mensagem': 'Conta Criada!'
        }
        criar_colunas_iniciais(user)
        return HttpResponse(json.dumps(retorno), content_type='application/json')

    return render(request, 'home/sign_up.html')


def verificar_email_ja_existente(request):
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


def handler_404(request, exception):
    return render(request, 'home/error_404.html')


def handler_500(request):
    return render(request, 'home/error_404.html')


