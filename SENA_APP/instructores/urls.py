from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructores, name='instructores'),
    path('detalle/<str:documento>/', views.detalle_instructor, name='detalle_instructor'),
]
