from django.contrib import admin


from .models import Curso

@admin.register(Curso)
class CursoResource(admin.ModelAdmin):
    model = Curso
    list_display = ("title", "created_at")
    
 