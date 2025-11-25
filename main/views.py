from django.shortcuts import render

from cursos.models import Curso
from blog.models import Post


def home_views(request):
    context = {
        'posts': Post.objects.filter(show_home=True),
        'cursos': Curso.objects.filter(show_home=True),
    }
    return render(request, 'main/home.html', context)


def about_us_views(request):
    return render(request, 'main/about_us.html')


def login_views(request):
    return render(request, 'main/login.html')


def register_views(request):
    return render(request, 'main/register.html')


def contact_views(request):
    return render(request, 'main/contact.html')