from django.urls import path
from .views import about_us_views, contact_views, home_views, login_views, register_views, logout_views, Prueba, PruebaTemplateView, ContactFormView

app_name = "main"

urlpatterns = [
    path('about_us/', about_us_views, name="about_us"),
    path('contact/', contact_views, name="contact"),
    path('contact/ccbv/', ContactFormView.as_view(), name="contact_ccbv"),
    path('', home_views, name="home"),
    path('login/', login_views, name="login"),
    path('logout/', logout_views, name="logout"),
    path('register/', register_views, name="register"),
    path('prueba/', Prueba.as_view(), name="prueba"),
    path('pruebatemplateview/', PruebaTemplateView.as_view(), name="prueba_template_view"),
]