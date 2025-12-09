from django.urls import path
from . import views

app_name = 'aprendices'

urlpatterns = [
    path('datos_aprendices/', views.aprendices, name='datos_aprendices'),
    path('detalle/<int:id>/', views.detalle_aprendices, name='detalle_aprendices'),
    path('', views.main, name='main'),
    path('aprendices/crear/', views.AprendizCreateView.as_view(), name='crear_aprendiz'),
]
