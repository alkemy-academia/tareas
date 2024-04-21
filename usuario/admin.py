from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from usuario.models import Usuario


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    search_fields = ['username']

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Agregar el campo dni al fieldset 'Personal info'
        if obj:
            fieldsets[1][1]['fields'] += ('documento_identidad',)
        return fieldsets
