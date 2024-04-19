from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    asignada_a = models.ForeignKey('usuario.Usuario', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.titulo
