from django.urls import path
from .views import cursos_views, cursos_detail_views

app_name = "cursos"

urlpatterns = [
    path('', cursos_views, name="cursos_list"),
    path('<int:id>/', cursos_detail_views, name="cursos_detail"),
]