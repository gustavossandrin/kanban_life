from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from kanban_life.board.models import Column, Task
from django.views import View


@method_decorator([login_required, csrf_exempt], name='dispatch')
class BoardIndexView(View):
    def get(self, request, id):
        if request.user.id != id:
            return render(request, 'home/error_404.html')

        columns = Column.objects.filter(user_id=id).order_by('position')

        for column in columns:
            tasks = Task.objects.filter(column=column)
            column.tasks = tasks

        return render(request, 'board/board.html', {'colunas': columns, 'kanban_id': id})


@method_decorator([login_required, csrf_exempt], name='dispatch')
class CreateTaskView(View):
    def post(self, request):
        column_id = request.POST['coluna_id']
        task_name = request.POST['tarefa_nome']

        task = Task()
        task.column_id = column_id
        task.name = task_name
        task.save()