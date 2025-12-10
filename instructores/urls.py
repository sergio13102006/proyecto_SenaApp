from django.urls import path
from . import views

app_name = 'instructores'

urlpatterns = [

    path('', views.instructores, name='lista_instructores'),
    
    path('instructor/<str:documento_identidad>/', views.detalle_instructor, name='detalle_instructor'),
    
    path('crear/', views.InstructorCreateView.as_view(), name='agregar_instructor'),

    path('<str:documento_identidad>/editar/', views.InstructorUpdateView.as_view(), name='editar_instructor'),

    path('<str:documento_identidad>/eliminar/', views.InstructorDeleteView.as_view(), name='eliminar_instructor'),
]
