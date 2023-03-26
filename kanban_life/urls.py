"""kanban_life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from kanban_life.home.views import home, about, sign_up, verificar_email_ja_existente, handler_404, handler_500
from kanban_life.login.views import login_index
from kanban_life.board.views import board_index

handler404 = handler_404
handler500 = handler_500
urlpatterns = [
    path('admin/', admin.site.urls),
    # HOME
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('sign_up/', sign_up, name='sign_up'),
    path('verificar_email_ja_existente/', verificar_email_ja_existente, name='verificar_email_ja_existente'),
    # LOGIN
    path('login/', login_index, name='login_index'),
    # BOARD
    path('board/<int:id>', board_index, name='board_index'),
]
