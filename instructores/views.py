from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import instructor
from django.urls import reverse_lazy
from instructores.forms import InstructorForm
from django.views import generic    
from django.contrib import messages
from django.views.generic import FormView

def instructores(request):
    lista_instructor = instructor.objects.all().values()
    template = loader.get_template('lista_instructores.html')
    context = {
        'lista_instructores': lista_instructor,   
        'total_instructores': instructor.objects.all().count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_instructor(request, documento_identidad):
    instructor_obj = instructor.objects.get(documento_identidad=documento_identidad)
    template = loader.get_template('detalle_instructor.html')
    context = {
        'instructor': instructor_obj,
    }
    return HttpResponse(template.render(context, request))


class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = instructor
    form_class = InstructorForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un instructor existente"""
    model = instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    pk_url_kwarg = 'documento_identidad'
    success_url = reverse_lazy('instructores:lista_instructores')

    
    def form_valid(self, form):
        messages.success(
            self.request,
            f'El instructor {form.instance.nombre} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)


class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
    pk_url_kwarg = 'documento_identidad'
    
    def delete(self, request, *args, **kwargs):
        instructor = self.get_object()
        messages.success(
            request,
            f'El instructor {instructor.nombre()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)