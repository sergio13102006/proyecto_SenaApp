from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_curso, name='lista_curso'),
    path('<int:codigo>/', views.detalle_curso, name='detalle_cursos'),
]
