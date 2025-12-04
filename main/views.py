from django.shortcuts import render

from cursos.models import Curso
from blog.models import Post

from .form import ContactForm, LoginForm, UserRegisterForm
from django.core.mail import send_mail
from .models import Contact

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from django.urls import reverse

from django.contrib.auth.models import User



def home_views(request):
    context = {
        'posts': Post.objects.filter(show_home=True),
        'cursos': Curso.objects.filter(show_home=True),
    }
    return render(request, 'main/home.html', context)


def about_us_views(request):
    return render(request, 'main/about_us.html')


def login_views(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('main:home'))
            else:
                context = {
                    'form': form,
                    'error': True,
                    'error_message': 'Usuario no válido'
                }
            return render(request, 'main/login.html', context)  
        else: 
            context = {
                'form': form,
                'error': True
            }     
            return render(request, 'main/login.html', context)  
    else:
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, 'main/login.html', context)

def logout_views(request):
    logout(request)
    return redirect(reverse('main:home'))

def register_views(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']  

            user = User.objects.create_user(username, email, password1)  
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.save()

            context = {
                "msj": 'Usuario creado correctamente'
            }

            return render(request, 'main/register.html', context)
        else:
            context = {
                'form': form,
                'error': True
            }  
            return render(request, 'main/register.html', context)
    else:
        form = UserRegisterForm()
        context = {
            "form": form
        }
    return render(request, 'main/register.html', context)


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

            Contact.objects.create(
                nombre=nombre,
                email=email,
                comentario=comentario
            )
            success = send_mail(
                "Formulario de contacto de mi web",
                message_content,
                "mendozagonzalez.irene@gmail.com",
                ["iremen19@gmail.com", "mendozagonzalez.irene@gmail.com"],
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