from django.shortcuts import render


def home_views(request):
    return render(request, 'main/home.html')


def about_us_views(request):
    return render(request, 'main/about_us.html')


def login_views(request):
    return render(request, 'main/login.html')


def register_views(request):
    return render(request, 'main/register.html')


def contact_views(request):
    return render(request, 'main/contact.html')