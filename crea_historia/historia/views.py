# historia/views.py
from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'La aventura comienza',
        'texto': 'Te despiertas en un mundo desconocido. Frente a ti hay dos caminos.',
        'imagen': 'aventura.png' # <--- ¡CAMBIA ESTO! Debe ser el nombre del archivo local
    }
    return render(request, 'historia/pagina.html', contexto)

def bosque(request):
    contexto = {
        'titulo': 'El bosque encantado',
        'texto': 'El bosque es oscuro, pero sientes una energía extraña a tu alrededor.',
        'imagen': 'bosque.png'  # <--- CAMBIAR POR EL NOMBRE DE TU ARCHIVO
    }
    return render(request, 'historia/pagina.html', contexto)

def cueva(request):
    contexto = {
        'titulo': 'La cueva misteriosa',
        'texto': 'Dentro de la cueva escuchas ruidos inquietantes.',
        'imagen': 'cueva.png'  # <--- CAMBIAR POR EL NOMBRE DE TU ARCHIVO
    }
    return render(request, 'historia/pagina.html', contexto)

# Asegúrate de que las funciones final_bueno y final_malo también usen nombres de archivos locales:
def final_bueno(request):
    contexto = {
        'titulo': 'Final feliz',
        'texto': '¡Has sobrevivido a la aventura!',
        'imagen': 'final_bueno.png' # <--- CAMBIAR POR EL NOMBRE DE TU ARCHIVO
    }
    return render(request, 'historia/final.html', contexto)

def final_malo(request):
    contexto = {
        'titulo': 'Fin de la aventura',
        'texto': 'Has caído en una trampa...',
        'imagen': 'final_malo.png' # <--- CAMBIAR POR EL NOMBRE DE TU ARCHIVO
    }
    return render(request, 'historia/final.html', contexto)