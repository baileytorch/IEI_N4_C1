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
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre Autor...',
                    'type':'text'
                }
            ),
            'pseudonimo': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Pseudónimo Autor...',
                    'type':'text'
                }
            ),
            'nacionalidad': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'fecha_defuncion': forms.DateInput(
                format='%d-%m-%Y',
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'biografia': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Biografía Autor...',
                    'type':'text',
                    'rows':'5'
                }
            )          
        }

class DeshabilitarAutorForm(forms.ModelForm):
    class Meta:
        model = mod.Autor
        fields = ['habilitado']