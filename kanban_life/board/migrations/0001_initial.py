# Generated by Django 5.1.3 on 2024-12-02 18:23

import django.utils.timezone
import model_utils.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('position', models.IntegerField(verbose_name='Posição')),
                ('max_task', models.IntegerField(blank=True, null=True, verbose_name='Número Máximo de Tarefas')),
                ('final_column', models.BooleanField(default=False, verbose_name='Coluna Final')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300, verbose_name='Nome da Tarefa')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Tempo da Tarefa')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição da Tarefa')),
                ('position', models.IntegerField(default=1, verbose_name='Posição Coluna')),
                ('color', models.CharField(blank=True, choices=[('yellow', 'Yellow'), ('green', 'Green'), ('blue', 'Blue'), ('red', 'Red'), ('cyan', 'Cyan'), ('orange', 'Orange'), ('purple', 'Purple'), ('magenta', 'Magenta')], max_length=10, null=True, verbose_name='Cor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]