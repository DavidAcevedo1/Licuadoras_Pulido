from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib import messages
from administrador.views import tipoelemento
from usuarios.models import Producto
from .Carrito import Carrito
from administrador.models import Elemento, Tipos_Elemento

def inicio(request):
    titulo_pagina='Inicio'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
     
    return render(request, "index.html", context)

def accesorio(request):
    titulo_pagina='Accesorios'
    subcategorias= Tipos_Elemento.objects.filter(categoria="Accesorios")
    elementos = Elemento.objects.filter(tipo_elemento__categoria="Accesorios")
    context={
        "subcategorias":subcategorias,
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/accesorios.html", context)

def producto(request):
    titulo_pagina='Productos'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/productos.html", context)

def serviciocliente(request):
    titulo_pagina='Servicios Cliente'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/servicioscliente.html", context)

def nosotros(request):
    titulo_pagina='Nosotros'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/nosotros.html", context)

def politicasprivacidad(request):
    titulo_pagina='Politicas de Privacidad'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/politicasprivacidad.html", context) 
    
def carrito(request):
    titulo_pagina='Carrito'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/carrito.html", context)

def agregar_elemento(request, elemento_id):   
    carrito = Carrito(request) 
    elemento = Elemento.objects.get(id=elemento_id) 
    carrito.agregar(elemento=elemento)

    return redirect("usuarios-carrito")

def eliminar_elemento(request, elemento_id):
    carrito = Carrito(request)
    elemento = Elemento.objects.get(id=elemento_id)
    carrito.eliminar(elemento=elemento)
    
    return redirect("usuarios-carrito")

def restar_elemento(request, elemento_id):
    carrito = Carrito(request)
    elemento = Elemento.objects.get(id=elemento_id)
    carrito.restar(elemento=elemento)
    
    return redirect("usuarios-carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    
    return redirect("usuarios-carrito")