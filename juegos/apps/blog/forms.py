from django import forms
from .models import Articulo
from django.core.exceptions import ValidationError


# Widget custom para permitir múltiples archivos
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class ArticuloForm(forms.ModelForm):
    # Campo de imágenes gestionado en la vista (se usa request.FILES.getlist('imagenes'))

    class Meta:
        model = Articulo
        fields = ['titulo', 'contenido', 'categoria']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'textarea_custom1',
                'rows': 10,
                'cols': 80,
                'style': 'resize:none;'
            }),
        }

