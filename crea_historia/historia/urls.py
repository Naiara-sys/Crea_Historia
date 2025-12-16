# crea_historia/historia/urls.py
from django.urls import path
from . import views # Importa las vistas (funciones) de esta misma carpeta

urlpatterns = [
    path('', views.inicio, name='inicio'), # Mapea la ruta raíz ('/') a la función inicio
    path('bosque/', views.bosque, name='bosque'),
    path('cueva/', views.cueva, name='cueva'),
    path('final-bueno/', views.final_bueno, name='final_bueno'),
    path('final-malo/', views.final_malo, name='final_malo'),
]