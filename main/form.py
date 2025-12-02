from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre:", 
        max_length=50)
    email = forms.EmailField(
        label="Email:"
    )
    comentario = forms.CharField(
        label="Comentario:", 
        max_length= 1000,
        widget=forms.Textarea
    )

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre)<5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres")
        return nombre
    
    