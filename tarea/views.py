from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from tarea.models import Tarea

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea/lista_tareas.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'tarea/detalle_tarea.html', {'tarea': tarea})

@permission_required('tarea.add_tarea', raise_exception=True)
def crear_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        completado = True if request.POST.get('completado') == 'on' else False
        Tarea.objects.create(titulo=titulo, descripcion=descripcion, completado=completado)

        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_form.html')

@login_required
@permission_required('tarea.change_tarea', raise_exception=True)
def modificar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        completado = True if request.POST.get('completado') == 'on' else False
        tarea.titulo = titulo
        tarea.descripcion = descripcion
        tarea.completado = completado
        tarea.save()

        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_form.html', {'tarea': tarea})

@login_required
@permission_required('tarea.delete_tarea', raise_exception=True)
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_confirm_delete.html', {'tarea': tarea})
