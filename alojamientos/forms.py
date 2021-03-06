from django import forms
from .models import Alojamiento, Comentario

class AlojamientoForm(forms.ModelForm):

    class Meta:
        model = Alojamiento
        fields = ("titulo", "barrio", "direccion", "telefono", "texto",)



class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ("texto",)
