from django.shortcuts import render
from .models import Curso
from django.contrib.auth.decorators import login_required

@login_required
def cursos_views(request):
    if not request.user.is_authenticated:
        return redirect("/")
 
    all_cursos = Curso.objects.all()

    context = {
        "cursos": all_cursos
    }
    return render(request, 'cursos/cursos.html', context)

@login_required
def cursos_detail_views(request, id):
    curso = Curso.objects.get(pk=id)

    context = {
        "curso": curso
    }

    return render(request, 'cursos/cursos_detail.html', context)
