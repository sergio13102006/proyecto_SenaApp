from django.urls import path
from . import views

urlpatterns = [
    path('', views.programas, name='lista_programas'),
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
]
