# historia/views.py
from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'La aventura comienza',
        'texto': 'Te despiertas en un mundo desconocido. Frente a ti hay dos caminos.',
        'imagen': 'aventura.jpg' # <--- ¡CAMBIA ESTO! Debe ser el nombre del archivo local
    }
    return render(request, 'historia/pagina.html', contexto)

def bosque(request):
    contexto = {
        'titulo': 'El bosque encantado',
        'texto': 'El bosque es oscuro, pero sientes una energía extraña. ¿Qué harás ahora?',
        'imagen': 'bosque.png' 
    }
    # CAMBIO CRÍTICO: Usar decision.html
    return render(request, 'historia/decision.html', contexto) 

def cueva(request):
    contexto = {
        'titulo': 'La cueva misteriosa',
        'texto': 'Dentro de la cueva escuchas ruidos inquietantes. ¿A dónde irás?',
        'imagen': 'cueva.png' 
    }
    # CAMBIO CRÍTICO: Usar decision.html
    return render(request, 'historia/decision.html', contexto)

def final_bueno(request):
    contexto = {
        'titulo': 'Final feliz',
        'texto': '¡Has sobrevivido a la aventura!',
        'imagen': 'primerfin.png'
    }
    return render(request, 'historia/final.html', contexto)

def final_malo(request):
    contexto = {
        'titulo': 'Fin de la aventura',
        'texto': 'Has caído en una trampa...',
        'imagen': 'segundofin.png' 
    }
    return render(request, 'historia/final.html', contexto)