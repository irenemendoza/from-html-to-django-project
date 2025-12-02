from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactResource(admin.ModelAdmin):
    model = Contact
    list_display = ("nombre", "email", "comentario", "created_at", "contacted")
    list_filter = ("contacted", )