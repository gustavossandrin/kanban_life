from django.contrib import admin
from django.urls import path
from kanban_life.home.views import home, about, sign_up, verificar_email_ja_existente, handler_404, handler_500
from kanban_life.login.views import login_index, login_exit
from kanban_life.board.views import BoardIndexView, CreateTaskView

handler404 = handler_404
handler500 = handler_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('sign_up/', sign_up, name='sign_up'),
    path('verificar_email_ja_existente/', verificar_email_ja_existente, name='verificar_email_ja_existente'),
    path('login/', login_index, name='login_index'),
    path('login/exit/', login_exit, name='login_exit'),
    path('board/<int:id>', BoardIndexView.as_view(), name='board_index'),
    path('board/criar_tarefa/', CreateTaskView.as_view(), name='criar_tarefa'),
]
