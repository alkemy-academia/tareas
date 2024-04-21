from django.contrib import admin

from tarea.models import Tarea


# Register your models here.
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'completado', 'asignada_a']
    search_fields = ['titulo', 'asignada_a__username']
    list_filter = ['completado']
    autocomplete_fields = ['asignada_a']
