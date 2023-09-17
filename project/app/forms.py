from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *

class CompraForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = Compra
        fields = ['data_compra', 'produto', 'quantidade', 'preco']

class VendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Venda
        fields = ['data_venda', 'quantidade', 'preco_total']

class PeriodoForm(forms.Form):
    periodo_inicio = forms.DateField(label='Data de início')
    periodo_fim = forms.DateField(label='Data de término')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'