from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('datos_aprendices/', views.aprendices, name='datos_aprendices'),
    path('detalle/<str:documento_identidad>/', views.detalle_aprendices, name='detalle_aprendices'),
    path('', views.main, name='main'),
    path('aprendices/crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
    path('aprendices/<str:documento_identidad>/editar/', views.AprendizUpdateView.as_view(), name='editar_aprendiz'),
    path('aprendices/<str:documento_identidad>/eliminar/', views.AprendizDeleteView.as_view(), name='eliminar_aprendiz'),
]