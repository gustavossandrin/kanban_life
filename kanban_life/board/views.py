from django.contrib.auth.decorators import login_required

from django.shortcuts import render


# Create your views here.

@login_required
def board_index(request, id):
    tgeste = 1 + 1
    if request.user.id != id:
        pass
    return render(request, 'board/board.html')
