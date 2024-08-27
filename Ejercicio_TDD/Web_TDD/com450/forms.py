from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = '__all__'
        widgets = {
            'observaciones': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }