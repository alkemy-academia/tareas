from django.urls import path
from . import views

app_name = 'tarea'

urlpatterns = [
    path('lista_tareas/', views.lista_tareas, name='lista_tareas'),
    path('detalle_tarea/<int:pk>/', views.detalle_tarea, name='detalle_tarea'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('modificar_tarea/<int:pk>/', views.modificar_tarea, name='modificar_tarea'),
    path('eliminar_tarea/<int:pk>/', views.eliminar_tarea, name='eliminar_tarea'),
]
