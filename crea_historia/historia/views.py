# historia/views.py
from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'La aventura comienza',
        'texto': 'Te despiertas en un mundo desconocido. Frente a ti hay dos caminos.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/pagina.html', contexto)

def bosque(request):
    contexto = {
        'titulo': 'El bosque encantado',
        'texto': 'El bosque es oscuro, pero sientes una energía extraña a tu alrededor.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/pagina.html', contexto)

def cueva (request):
    contexto = {
        'titulo': 'La cueva misteriosa',
        'texto': 'Dentro de la cueva escuchas ruidos inquietantes.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/pagina.html', contexto)

def final_bueno (request):
    contexto = {
        'titulo': 'Final feliz',
        'texto': 'Has tomado buenas decisiones y consigues salir con vida.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render (request, 'historia/final.html', contexto)

def final_malo(request):
    contexto = {
        'titulo': 'Final triste',
        'texto': 'Tus decisiones te han llevado a un final desafortunado.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/final.html', contexto)