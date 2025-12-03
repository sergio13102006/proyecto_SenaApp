from django.urls import path
from . import views

urlpatterns = [
    path('aprendices/', views.aprendices, name='aprendices'),
    path('datos_aprendices/', views.aprendices, name='datos_aprendices'),
    path('', views.main, name='main'),
]
