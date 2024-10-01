from django.db import models


COR_CHOICES = (
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('cyan', 'Cyan'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('magenta', 'Magenta'),
)


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


class Tarefa(models.Model):
    tarefa_coluna = models.ForeignKey(
        'board.TarefaColuna',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    nome = models.CharField(
        u'Nome da Tarefa',
        null=False,
        blank=False,
        max_length=300,
    )

    tempo = models.TimeField(
        u'Tempo da Tarefa',
        null=True,
        blank=True,
        auto_now=False,
        auto_now_add=False,
    )

    descricao = models.CharField(
        u'Descrição da Tarefa',
        max_length=500,
        null=True,
        blank=True,
    )

    posicao = models.IntegerField(
        u'Posição Coluna',
        blank=False,
        null=False,
        default=1,
    )

    cor = models.CharField(
        u'Dia Da Semana',
        max_length=10,
        choices=COR_CHOICES,
        null=True,
        blank=True,
    )
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



