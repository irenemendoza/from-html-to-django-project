from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField


class Curso(models.Model):
    title = models.CharField(
        verbose_name = "Título",
        max_length = 200)
    
    content = RichTextField(
        verbose_name = "Contenido"
    )
    
    call_link = models.URLField(
        verbose_name = "Enlace de llamada"
    )
    
    created_at = models.DateTimeField(
        verbose_name = "Fecha de creación",
        default = timezone.now)
    
    show_home = models.BooleanField(
        'Mostrar en la home',
        default=False
    )

    toc = models.FileField(
        "Temario",
        upload_to="cursos/toc/",
        null=True,
        blank=True,
    )

    curso_image = ImageField(
        "Imagen del curso",
        upload_to="cursos/images/",
        null=True,
        blank=True,
    )
   
    def __str__(self):
        return self.title