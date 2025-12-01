from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'se_core/index.html')


def misionYVision(request):
    return render(request, 'se_core/mision.html')

def contactanos(request):
    return render(request, 'se_core/contactanos.html')


def acercaDe(request):
    return render(request, 'se_core/acerca_de.html')


def iniciarSesion(request):
    return render(request, 'se_core/login.html')


def inicioSesion(request):
    return HttpResponse("Iniciando Sesión... en construcción")


def registrarme(request):
    return render(request, 'se_core/registro.html')