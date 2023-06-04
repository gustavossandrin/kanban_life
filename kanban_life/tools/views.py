from django.shortcuts import render


# Create your views here.
from kanban_life.board.models import TarefaColuna


def criar_colunas_iniciais(user):
    # primira coluna
    coluna_1 = TarefaColuna()
    coluna_1.user = user
    coluna_1.nome = 'To-do'
    coluna_1.posicao = 1
    coluna_1.save()

    # Segunda coluna
    coluna_2 = TarefaColuna()
    coluna_2.user = user
    coluna_2.nome = 'Do Today'
    coluna_2.posicao = 2
    coluna_2.save()

    # Terceira Coluna
    coluna_3 = TarefaColuna()
    coluna_3.user = user
    coluna_3.nome = 'In progress'
    coluna_3.posicao = 3
    coluna_3.maximo_de_tarefas = 3
    coluna_3.save()

    coluna_4 = TarefaColuna()
    coluna_4.user = user
    coluna_4.nome = 'Done'
    coluna_4.posicao = 4
    coluna_4.coluna_final = True
    coluna_4.save()


