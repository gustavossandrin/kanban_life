from django.contrib import admin
from django.urls import path
from kanban_life.home.views import HomeView, AboutView, SignUpView, VerifyEmail, handler_404, handler_500
from kanban_life.login.views import login_index, login_exit
from kanban_life.board.views import BoardIndexView, CreateTaskView

handler404 = handler_404
handler500 = handler_500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('verificar_email_ja_existente/', VerifyEmail.as_view(), name='verificar_email_ja_existente'),
    path('login/', login_index, name='login_index'),
    path('login/exit/', login_exit, name='login_exit'),
    path('board/<int:id>', BoardIndexView.as_view(), name='board_index'),
    path('board/criar_tarefa/', CreateTaskView.as_view(), name='criar_tarefa'),
]
