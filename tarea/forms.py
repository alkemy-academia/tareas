from django import forms
from django.core.exceptions import ValidationError

from tarea.models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo', 'descripcion', 'completado', 'asignada_a'
        ]

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise ValidationError('El título debe tener al menos 5 caracteres.')
        return titulo

    def clean(self):
        cleaned_data = super().clean()
        completado = self.cleaned_data.get('completado')
        asignada_a = self.cleaned_data.get('asignada_a')
        if completado and not asignada_a:
            raise ValidationError({'completado': 'Una tarea completada debe tener un Usuario asignado.'}, code='invalido')
        return cleaned_data
