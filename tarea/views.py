from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from tarea.forms import TareaForm
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
    nueva_tarea = None
    if request.method == 'POST':
        tarea_form = TareaForm(request.POST)
        if tarea_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_tarea = tarea_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la Tarea {}'.format(nueva_tarea))
            return redirect(reverse('tarea:detalle_tarea', args={nueva_tarea.id}))
    else:
        tarea_form = TareaForm()

    return render(request, 'tarea/tarea_form.html',
                  {'form': tarea_form})


@login_required
@permission_required('tarea.change_tarea', raise_exception=True)
def modificar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form_tarea = TareaForm(request.POST, instance=tarea)
        if form_tarea.is_valid():
            form_tarea.save()
            messages.success(request, 'Se ha actualizado correctamente la Tarea')
            return redirect(reverse('tarea:detalle_tarea', args=[tarea.id]))
    else:
        form_tarea = TareaForm(instance=tarea)

    return render(request, 'tarea/tarea_form.html', {'form': form_tarea})


@login_required
@permission_required('tarea.delete_tarea', raise_exception=True)
def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect(reverse('tarea:lista_tareas'))

    return render(request, 'tarea/tarea_confirm_delete.html', {'tarea': tarea})
