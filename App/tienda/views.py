from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.db import IntegrityError

# vistas basasdas en funciones


def prueba(request):
    return HttpResponse("<h1 style='color:#000fff;'> Hola mundo </h1>")


def user(request):
    return HttpResponse(
        "<h1 style='color:Green;'> Juan Camilo Gallego Jurado</h1>"
        "<a href='../prueba/'>Link</a>"
    )


def index(request):
    # return HttpResponse("Index")
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
    return HttpResponse(
        f"Su nombre es <b>{nombre}</b> y <b>{hambre}</b> tiene hambre!!"
    )


def sumar_formulario(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        # return HttpResponse(f"la suma de {n1} + {n2} es <strong>{n1+n2}</strong>")
        contexto = {"n1": n1, "n2": n2, "respuesta": n1 + n2}

        return render(
            request,
            "sumar_respuesta.html",contexto
        )
    else:
        return render(request, "sumar_formulario.html")


#CRUD

def productos(request):
    produ = Product.objects.all()
    
    contexto = {
        "datos":produ
    }
    return render(request,"productos/lista_productos.html", contexto) 

def eliminar_producto(request, id_produc):
    try:
        produ = Product.objects.get(id=id_produc)
        produ.delete()
        # return HttpResponse(f"Producto {produ.name} eliminado correctamente")
        messages.success(request, f"Producto {produ.name} eliminado correctamente")
    except Product.DoesNotExist:
        # return HttpResponse(f"El producto {produc.name} no existe")
        messages.warning(request, f"El producto {produ.name} no existe")
    except IntegrityError:
        # return HttpResponse("Error al eliminar el producto relacionado con otra tabla")
        messages.error(request, f"Error al eliminar el producto relacionado con otra tabla")
    except Exception as e:
        # return HttpResponse(f"Error al eliminar el producto  {e}")
        messages.error(request, f"Error al eliminar el producto  {e}")
    return redirect("productos")

def editar_producto(request, id_produc):
    pass

def agregar_producto(request):
    if request.method == "POST":
        cod = request.POST.get("cod")
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        CATEGORIAS = request.POST.get("categoria")
        try:
            q = Product(
                cod=cod,
                nombre=nombre,
                precio=precio,
                stock=stock,
                categoria=CATEGORIAS
            )
            q.save()
            messages.success(request, f"Producto {q.nombre} agregado correctamente")
        except Exception as e:
            messages.error(request, f"Error al agregar el producto {e}")
        return redirect("productos")
    else:
        return render(request, "productos/agregar_productos.html")        
        