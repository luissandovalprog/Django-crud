# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock"]

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio <= 0:
            raise ValidationError("El precio debe ser un valor mayor a 0.")
        return precio

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre and len(nombre.strip()) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres válidos.")
        return nombre