from django.http import HttpResponse
from django.template import loader
from .models import Curso


def lista_curso(request):
  cursos = Curso.objects.all()
  template = loader.get_template('lista_curso.html')
  context = {
     'cursos': cursos,
    'total_cursos': cursos.count(),
   }
  return HttpResponse(template.render(context, request))
def detalle_curso(request, codigo):
    curso = Curso.objects.get(id=codigo)
    template = loader.get_template('detalle_cursos.html')
    context = {
        'curso': curso,
    }
    return HttpResponse(template.render(context, request))
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
