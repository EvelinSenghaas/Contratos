from django import forms
from .models import *

class EstadoForm(forms.ModelForm):
    class Meta:
        model=Estado
        fields=['estado']
        widgets={
            'estado': forms.TextInput(attrs={'class':'form-control'}),
        }

class ObjetoForm(forms.ModelForm):
    class Meta:
        model=Objeto
        fields=['descripcion']
        widgets={
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model=Solicitante
        fields=['solicitante']
        widgets={
            'solicitante': forms.TextInput(attrs={'class':'form-control'}),
        }

class ContratoForm(forms.ModelForm):
    class Meta:
        model=Contrato
        fields=['fecha_d','fecha_h','nro_dis','estado','resumen','fecha_c','anexo','solicitante','persona','contrato','objeto','nombre_archivo']
        widgets={
            'fecha_d':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fecha_h':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'nro_dis':forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'resumen':forms.TextInput(attrs={'class':'form-control'}),
            'nombre_archivo':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_c':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'anexo':forms.TextInput(attrs={'class':'form-control'}),
            'solicitante': forms.Select(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'contrato':forms.TextInput(attrs={'class':'form-control'}),
            'objeto': forms.Select(attrs={'class':'form-control'}),
        }
    