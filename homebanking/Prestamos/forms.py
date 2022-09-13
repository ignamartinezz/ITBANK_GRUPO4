from dataclasses import fields
from django import forms
from .models import Prestamo
import datetime

# class FormPrestamo(forms.Form):
#     loan_total = forms.IntegerField(label="loan_total", required=True)
#     loan_type = forms.CharField(label="loan_type", required=True)

class PrestamoForm(forms.ModelForm):
    class Meta:
        model=Prestamo
        fields="__all__"

   
#    customer_id = forms.CharField(label="cliente_id", required=True)
#    loan_date = forms.DateField(
 #       label='Fecha de prestamo', initial=datetime.date.today)
 #   loan_total = forms.IntegerField(label='Monto del prestamo', required=True)