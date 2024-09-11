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




