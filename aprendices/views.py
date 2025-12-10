from django.http import HttpResponse
from django.template import loader
from .models import aprendiz
from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages


def aprendices(request):
    datos_aprendices = aprendiz.objects.all().values()
    template = loader.get_template('datos_aprendices.html')

    context = {
        'datos_aprendices': datos_aprendices,
        'total_aprendices': datos_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))

def detalle_aprendices(request, id):
    aprendizz = aprendiz.objects.get(id=id)
    template = loader.get_template('detalle_aprendices.html')
    context = {
        'aprendiz': aprendizz,
    }
    return HttpResponse(template.render(context, request))  
# VISTAS BASADAS EN CLASES - CRUD APRENDIZ

# CREATE - APRENDIZ

class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = aprendiz
    form_class = AprendizForm
    template_name = 'agregar_aprendiz.html'
    success_url = reverse_lazy('aprendices:datos_aprendices')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)
    
    
    
# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = aprendiz
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    success_url = reverse_lazy('aprendices:datos_aprendices')
    pk_url_kwarg = 'documento_identidad'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:datos_aprendices')
    pk_url_kwarg = 'documento_identidad'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)



def aprendices(request):
    myaprendices = aprendiz.objects.all()
    template = loader.get_template('datos_aprendices.html')
    context = {
        'myaprendices': myaprendices
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))