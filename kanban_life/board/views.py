from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

from django.shortcuts import render


# Create your views here.
from kanban_life.board.models import TarefaColuna, Tarefa


@login_required
def board_index(request, id):
    if request.user.id != id:
        return render(request, 'home/error_404.html')

    colunas = TarefaColuna.objects.filter(user_id=id).order_by('posicao')-

    for coluna in colunas:
        tarefas = Tarefa.objects.filter(tarefa_coluna_id=coluna.id)
        coluna.tarefas = tarefas

    return render(request, 'board/board.html', {'colunas': colunas})
