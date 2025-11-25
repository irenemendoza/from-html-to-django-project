from django.urls import path
from .views import blog_views, blog_detail_views

app_name = "blog"

urlpatterns = [
    path('', blog_views, name="blog_list"),
    path('<int:id>/', blog_detail_views, name="blog_detail"),
]

