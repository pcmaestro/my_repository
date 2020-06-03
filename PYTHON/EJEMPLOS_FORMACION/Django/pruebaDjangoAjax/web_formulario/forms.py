from django import forms
from . import models
from . import regexp
import re

class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(),
            "apellido_1": forms.TextInput(),
            "apellido_2": forms.TextInput(),
            "telefono": forms.NumberInput(),
            "email": forms.EmailInput(),
            "publicidad": forms.CheckboxInput()
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        validacion_nombre = re.compile(regexp.patron_texto)
        if not validacion_nombre:
            raise forms.ValidationError("El formato del nombre no es correcto")
        else:
            return nombre
    def clean_apellido_1(self):
        apellido_1 = self.cleaned_data.get("apellido_1")
        validacion_apellido_1 = re.compile(regexp.patron_texto)
        if not validacion_apellido_1:
            raise forms.ValidationError("El formato del apellido no es correcto")
        else:
            return apellido_1

    def clean_apellido_2(self):
        apellido_2 = self.cleaned_data.get("apellido_2")
        validacion_apellido_2 = re.compile(regexp.patron_texto)
        if not validacion_apellido_2:
            raise forms.ValidationError("El formato del apellido no es correcto")
        else:
            return apellido_2

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        validacion_telefono = re.compile(regexp.patron_telefono)
        if not validacion_telefono:
            raise forms.ValidationError("El formato del tf no es correcto")
        else:
            return telefono

    def clean_email(self):
        email = self.cleaned_data.get("email")
        validacion_email = re.compile(regexp.patron_mail)
        if not validacion_email:
            raise forms.ValidationError("El formato del email no es correcto")
        else:
            return  email

