from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'textarea_custom1',
                'rows': 10,
                'cols': 80,
                'style': 'resize:none;',
            }),
        }
