from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel

COLOR_CHOICES = (
    ('yellow', 'Yellow'),
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('cyan', 'Cyan'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('magenta', 'Magenta'),
)


class Column(UUIDModel, TimeStampedModel):
    name = models.CharField(u'Nome', max_length=30)
    user = models.ForeignKey('home.User',on_delete=models.CASCADE)
    position = models.IntegerField(u'Posição')
    max_task = models.IntegerField(u'Número Máximo de Tarefas', blank=True, null=True)
    final_column = models.BooleanField(u'Coluna Final',default=False)


class Task(UUIDModel, TimeStampedModel):
    column = models.ForeignKey('board.Column',on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(u'Nome da Tarefa', null=False, blank=False, max_length=300)
    time = models.TimeField(u'Tempo da Tarefa', null=True, blank=True)
    description = models.CharField(u'Descrição da Tarefa', max_length=500, null=True, blank=True)
    position = models.IntegerField(u'Posição Coluna', default=1)
    color = models.CharField(u'Cor', max_length=10, choices=COLOR_CHOICES, null=True, blank=True)
