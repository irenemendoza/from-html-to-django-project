from django import forms
from django.contrib.auth.password_validation import validate_password


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
    
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Usuario", 
        max_length=20
        )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Contraseña",
        )

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Usuario", 
        max_length=20
        )
    first_name = forms.CharField(
        label="Nombre", 
        max_length=20
        )
    last_name = forms.CharField(
        label="Apellidos", 
        max_length=50
        )
    email = forms.EmailField(
        label="Email", 
        max_length=50
        )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Contraseña",
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label="Repite tu contraseña",
        )
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2 and password1 != "":
            raise forms.ValidationError(('Las constraseñas no coinciden'))
    
        if password2 != '':
            validate_password(password2)

        return password2