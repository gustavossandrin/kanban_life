from django.db import models


class TarefaColuna(models.Model):
    nome = models.CharField(
        u'Nome',
        max_length=30
    )
    user = models.ForeignKey(
        'home.User',
        on_delete=models.CASCADE
    )
    posicao = models.IntegerField(
        u'Posição Coluna',
        blank=False,
        null=False,
    )
    maximo_de_tarefas = models.IntegerField(
        u'Número Máximo de Tarefas',
        blank=True,
        null=True,
    )
    coluna_final = models.BooleanField(
        u'Coluna Final',
        default=False,
    )
    #  Dados de LOG
    criado_em = models.DateTimeField(
        u'Criado em',
        blank=True,
        null=True,
        auto_now_add=True,
    )
    alterado_em = models.DateTimeField(
        u'Alterado em',
        blank=True,
        null=True,
        auto_now=True,
    )


