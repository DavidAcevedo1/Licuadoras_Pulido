from django.shortcuts import render
from usuarios.Carrito import Carrito
from administrador.models import Elemento, Favorito
from facturas.models import  Factura
from facturas.forms import  FacturaForm
from django.contrib import messages
from usuarios.models import Rol, Usuario
from django.shortcuts import render, redirect
def inicio(request):
    favoritos= Elemento.objects.filter(favorito=True)
    print(favoritos)
    titulo_pagina='Inicio'
    carrito = Carrito(request) 
    context={
        "carrito": carrito,
        "favoritos":favoritos,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "index.html", context)

def inicio2(request):
    favoritos= Elemento.objects.filter(favorito=True)
    print(favoritos)
    titulo_pagina='factura'
    carrito = Carrito(request) 
    context={
        "carrito": carrito,
        "favoritos":favoritos,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "factura/factura.html", context)

def factura_eliminar(request,pk):
    titulo_pagina='Factura'
    tfacturas= Factura.objects.all()
    tfactura= Factura.objects.get(id=pk)
    accion_txt= f" la factura {tfactura.id}"
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        Factura.objects.filter(id=pk).update(
                    decision='Inactivo'
                )
        tfactura_usuario=  tfactura.usuario
        messages.success(request,f'Factura {tfactura.id} anulada correctamente')
        return redirect('factura-tfactura')
                
    else:
        form:FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "tfacturas": tfacturas,
            
    }
    return render(request, "factura/factura-eliminar.html", context)

def tfactura(request):
    factura=Factura.objects.filter(decision='Activo')
    titulo_pagina="Facturas"
    Rol_c=Rol.objects.all()
    Usuario_c=Usuario.objects.all()
    renew = '/factura/factura'
    tfacturas= Factura.objects.all()
    context={
        "factura":factura,
        "tfacturas": tfacturas,
        "renew":renew,
        "titulo_pagina":titulo_pagina,
        "Rol":Rol_c,
        "Usuario":Usuario_c
    }
    return render(request, "factura/factura.html",context)