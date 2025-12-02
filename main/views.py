from django.shortcuts import render

from cursos.models import Curso
from blog.models import Post

from .form import ContactForm
from django.core.mail import send_mail


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
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            comentario = formulario.cleaned_data['comentario']
            
            # Aquí deberías enviar el correo real
            print(f'Se ha enviado un correo a {nombre} al correo {email} con el texto {comentario}')
            
            message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

            success = send_mail(
                "Formulario de contacto de mi web",
                message_content,
                "info@laveladaconquer.com",
                ["iremen19@gmail.com"],
                fail_silently=False,
            )

            context = {
                "formulario": ContactForm(),  # Resetear el formulario después del éxito
                "success": success,
            }
            return render(request, 'main/contact.html', context)
    else:
        formulario = ContactForm()
    
    context = {
        "formulario": formulario
    }
    return render(request, 'main/contact.html', context)