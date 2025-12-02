from django.db import models
from django.utils import timezone

class Contact(models.Model):
    nombre = models.CharField(
        "Nombre",
        max_length = 50
        )
    email = models.EmailField(
        "Email"
    )
    comentario = models.TextField(
        "Comentario que ha dejado en la web"
    )

    created_at = models.DateTimeField(
        "Fecha y hora de creación",
        default=timezone.now
    )

    def __str__(self):
        return self.nombre