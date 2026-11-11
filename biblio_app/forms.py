from django import forms
from . import models as mod

class AutorForm(forms.ModelForm):
    class Meta:
        model = mod.Autor
        fields = [
            'nombre', 
            'pseudonimo', 
            'nacionalidad', 
            'fecha_nacimiento', 
            'fecha_defuncion', 
            'biografia']