from django.http import HttpResponse
from django.template import loader
from .models import aprendiz

def aprendices(request):
  myaprendices = aprendiz.objects.all()
  template = loader.get_template('datos_aprendices.html')
  context = {
    'myaprendices': myaprendices
  }
  return HttpResponse(template.render(context,request))
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))