from django.http import HttpResponse
from django.shortcuts import render

#vistas basasdas en funciones

def prueba(request):
    return HttpResponse("<h1 style='color:#000fff;'> Hola mundo </h1>")


def user(request):
    return HttpResponse("<h1 style='color:Green;'> Juan Camilo Gallego Jurado</h1>"
                        "<a href='../prueba/'>Link</a>")

def index(request):
    #return HttpResponse("Index")
    return render(request, "index.html")


def saludar(request, apellido):
    return HttpResponse(f"Hola {apellido}")

def suma(request, num1, num2):
    return HttpResponse(f"Resultado: {num1+num2}")

def encuesta_form(request):
    return render(request, "formulario_encuesta.html")

def procesar_encuesta(request):
    nombre = request.POST.get("name")
    hambre = request.POST.get("hambre")
    return HttpResponse(F"Su nombre es <b>{nombre}</b> y <b>{hambre}</b> tiene hambre!!")