from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound

from django.shortcuts import render


# Create your views here.

@login_required
def board_index(request, id):
    if request.user.id != id:
        return render(request, 'home/error_404.html')
    return render(request, 'board/board.html')
