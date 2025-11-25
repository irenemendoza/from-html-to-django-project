from django.db import models
from django.utils import timezone


class Curso(models.Model):
    title = models.CharField(
        verbose_name = "Título",
        max_length = 200)
    content = models.TextField(
        verbose_name = "Contenido"
    )
    call_link = models.URLField(
        verbose_name = "Enlace de llamada"
    )
    created_at = models.DateTimeField(
        verbose_name = "Fecha de creación",
        default = timezone.now)
   
    def __str__(self):
        return self.title