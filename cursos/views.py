from django.shortcuts import render
from .models import Curso

def cursos_views(request):
    all_cursos = Curso.objects.all()

    context = {
        "cursos": all_cursos
    }
    return render(request, 'cursos/cursos.html', context)

def cursos_detail_views(request, id):
    curso = Curso.objects.get(pk=id)

    context = {
        "curso": curso
    }

    return render(request, 'cursos/cursos_detail.html', context)
