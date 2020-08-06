from django import forms
from .models import *

class SexoForm(forms.ModelForm):
    class Meta:
        model=Sexo
        fields=['sexo']
        widgets={
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class PersonaForm(forms.ModelForm):
    class Meta:
        model=Persona
        fields=['cuit','dni','nombre','apellido','domicilio','email','fecha_nac','sexo','telefono']
        widgets = {
            'cuit': forms.TextInput(attrs={'class':'form-control','maxlength':'11'}),
            'dni': forms.TextInput(attrs={'class':'form-control','maxlength':'10'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'}),

        }


