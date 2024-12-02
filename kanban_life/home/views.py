import json
from django.http import HttpResponse
from django.shortcuts import render
from kanban_life.home.models import User
from kanban_life.tools.views import create_initial_columns
from django.views.generic import TemplateView
from django.views import View


class HomeView(TemplateView):
    template_name = 'home/home.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class SignUpView(TemplateView):
    template_name = 'home/sign_up.html'

    def post(self, request):
        full_name = request.POST['nome_completo']
        email = request.POST['email']
        password = request.POST['senha']

        user = User.objects.create_user(email, password, first_name=full_name)
        user.save()

        response = {
            'STATUS': 'OK',
            'mensagem': 'Conta Criada!'
        }
        create_initial_columns(user)
        return HttpResponse(json.dumps(response), content_type='application/json')


class VerifyEmail(View):
    def post(self, request):
        email = request.POST['email_verificar']
        users = User.objects.filter(email=email)

        retorno = {
            'STATUS': 'OK',
            'existe': users.exists()
        }

        return HttpResponse(json.dumps(retorno), content_type='application/json')


def handler_404(request, exception):
    return render(request, 'home/error_404.html')


def handler_500(request):
    return render(request, 'home/error_404.html')


