from django import forms
from .models import Prestamo
import datetime

typelist=[('1', 'PERSONAL'),  ('2', 'PRENDARIO'),
('3', 'HIPOTECARIO'), ('4', 'CONSUMO'), ('5', 'OTROS')]

class PrestamoForm(forms.Form):
    loan_type= forms.CharField(label="Tipo de prestamo", widget=forms.Select(choices=typelist))
    loan_date= forms.DateField(label="Fecha del prestamo", initial=datetime.date.today)
    loan_total = forms.IntegerField(label="Dinero del prestamo", required=True)


