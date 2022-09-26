from django.shortcuts import render, redirect
from django.template import context
from facturas.models import DetalleServicio, Factura, Detalle
from facturas.forms import DetalleServicioForm, FacturaForm, DetalleForm
from django.contrib import messages 
from usuarios.models import Rol, Usuario
from usuarios.Carrito import Carrito
from administrador.models import *
from django.db.models import Sum

def carrito(request):
    titulo_pagina='Carrito'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/carrito.html", context)

def factura(request):
    if request.method == 'POST':
        print(request.POST)
        aux= Factura.objects.create(
            tipofactura= request.POST['tipofactura']
        )
        messages.success(request,f'!La factura se agregó correctamente!')
        return redirect('factura-detalle',aux.id)
    else:
        messages.error(request,f'!Error al agregar Factura!')
    context={
        }
    
    return render(request,'factura/crearFactura.html', context)

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

def vfactura (request,pk):
    renew = 'hola mundo'
    titulo_pagina="Factura"
    factura= Factura.objects.get(id=pk)
    detalles= Detalle.objects.filter(factura_id=pk)
    print(detalles)
    context={
        "factura": factura,
        "titulo_pagina":titulo_pagina,
        "renew":renew,
        "detalles":detalles
    }
    return render(request,"factura/verfactura.html", context)
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

def detalle(request,pk):
    titulo_pagina="Detalle facturas"
    detalles= Detalle.objects.filter(factura_id=pk)
    cantidad2 = Elemento.objects.filter(id=pk)
    factura_u= Factura.objects.get(id=pk)
    elementos = Elemento.objects.filter(estado= "Activo")
    if factura_u.tipofactura == "Compra":
        rol_aux= "Proveedor"
        # rol_aux = Usuario.objects.filter(estado = " Activo", rol = "Proveedor")
    elif factura_u.tipofactura == "Venta": 
        rol_aux= "Cliente"   
        # usuario= Usuario.objects.filter(estado = " Activo", rol = "Cliente")
    else:
        rol_aux= "servicio"
    usuario= Usuario.objects.filter(rol=rol_aux, estado="Activo")
    servicio= Servicio.objects.all()
    if rol_aux != "servicio":
        if request.method == 'POST' and "form-detalle" in request.POST:
            form= DetalleForm(request.POST)
            detalle_aux= Detalle.objects.filter(factura_id=pk,elemento_id=request.POST['elemento'])
            if detalle_aux.exists():
                detalle_aux= Detalle.objects.filter(factura_id=pk,elemento_id=request.POST['elemento'])
            else:
                detalle_aux=None
            if detalle_aux == None:
                if form.is_valid():
                    factura= Detalle.objects.create(
                    cantidad=form.cleaned_data.get('cantidad'),
                    elemento= form.cleaned_data.get('elemento'),
                    factura=factura_u,        
                    )
                    if factura_u.tipofactura == "Venta":
                        
                       
                        elementosCapturados = request.POST["elemento"]
                        cantidad_stock = int(request.POST["cantidad"])
                        elemento = Elemento.objects.get(id=elementosCapturados).stock_elemento
                        Elemento.objects.filter(id = elementosCapturados ).update(
                                stock_elemento = elemento - cantidad_stock
                                )
                        print("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", elementosCapturados)
                        if cantidad_stock > elemento:
                            Detalle.objects.filter(id= elementosCapturados ).update(
                                cantidad = elemento 
                                )
                            cantidad_resta = Detalle.objects.get(id = elementosCapturados ).cantidad
                            Elemento.objects.filter(id = elementosCapturados ).update(
                                stock_elemento = elemento - cantidad_resta
                                )
                            precio = Elemento.objects.get(id =  elementosCapturados ).precio
                            Detalle.objects.filter(id = len(id) ).update(
                                total = precio * int(request.POST["cantidad"])
                                )
                            messages.warning(request,'La cantidad seleccionada a superado la cantidad que hay en el stock')
                        else:
                            Elemento.objects.filter(id=elementosCapturados).update(
                                stock_elemento = elemento   -  cantidad_stock
                                )
                            
                            precio = Elemento.objects.get(id =  elementosCapturados ).precio
                            id = Detalle.objects.values_list('id', flat=True)
                            Detalle.objects.filter(id = len(id) ).update(
                                total = precio * cantidad_stock
                                )
                            factura_id = Detalle.objects.get(id=len(id)).factura_id
                            items = Detalle.objects.get(id=len(id)).total

                            print ("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",factura_id) 
                            print("ññññññññññññññññññññññññññññññññññññññññññññññññññññññññ",items)
                            # total = precio * cantidad_stock
                    elif  factura_u.tipofactura == "Compra":
                        id = Detalle.objects.values_list('id', flat=True)
                        Elemento.objects.filter(id=elementosCapturados).update(
                            stock_elemento = elemento   +  cantidad_stock
                            )
                        precio = Elemento.objects.get(id =  elementosCapturados ).precio
                        id = Detalle.objects.values_list('id', flat=True)
                        Detalle.objects.filter(id = len(id) ).update(
                            total = precio * cantidad_stock
                        )
                    return redirect('factura-detalle', pk=pk)  
        else:
            form= DetalleForm()
    else:
        print("estamos aqui-----------------------------------------------------------------------")
        if request.method == 'POST' and "form-detalle" in request.POST:
            form= DetalleServicioForm(request.POST)
            detalle_aux= DetalleServicio.objects.filter(factura_id=pk, servicio_id=request.POST['servicio'])
            if detalle_aux.exists():
                detalle_aux= DetalleServicio.objects.filter(factura_id=pk, servicio_id=request.POST['servicio'])
            else:
                detalle_aux=None
            if detalle_aux == None:
                if form.is_valid():
                    factura= DetalleServicio.objects.create(
                    cantidad= form.cleaned_data.get('cantidad'),
                    servicio= form.cleaned_data.get('servicio'),
                    elemento= form.cleaned_data.get('elemento'),
                    costo= form.cleaned_data.get('costo'),
                    factura=factura_u,        
                    )
        else:
            form= DetalleServicioForm()
    if request.method == 'POST' and "form-serv" in request.POST:
        print(request.POST)
        if request.POST["servicio"] and request.POST["servicio"] != "--- Seleccione el servicio ---":
            usuario_final=Servicio.objects.get(id=request.POST["servicio"]).usuario
            Factura.objects.filter(id=pk).update(
                usuario=usuario_final,
                servicio= request.POST["servicio"]
            )
            return redirect('factura-detalle', pk=pk)
        else:
            print('Seleccione un sevicio!')
            messages.warning(request,f'Seleccione un servicio!')
    if request.method == 'POST' and "form-user" in request.POST:
        print(request.POST)
        if request.POST["usuario"] and request.POST["usuario"] != "null":
            usuario_final=Usuario.objects.get(Uid=request.POST["usuario"])
            Factura.objects.filter(id=pk).update(
                usuario=usuario_final,
            )
            return redirect('factura-detalle', pk=pk)
        else:
            print('Seleccione un usuario!')
            messages.warning(request,f'Seleccione un usuario!')
    context={
        "usuario":usuario,
        "servicio":servicio,
        "titulo_pagina": titulo_pagina,
        "detalles": detalles,
        "form":form,
        "factura":factura_u,
    }
    return render(request, "factura/detalle-factura.html", context)

def detalle_estado(request,pk ):
    titulo_pagina='elemento'
    url_eliminar='/factura/'
    detalle= Detalle.objects.get(id=pk)
    u_detalles= Detalle.objects.get(id=pk)
    factura_u= u_detalles.factura
    detalles= Detalle.objects.filter(factura_id=factura_u.id)
    accion_txt= f"Eliminando detalle {u_detalles.id}, una vez eliminado no hay marcha atras!"
    url_back = "/detalles/"
    if request.method == 'POST':
        form= DetalleForm(request.POST)
        form = DetalleForm(request.POST)
        u_detalles.delete()
        messages.success(request,f'El detalle de factura  se eliminó correctamente!')
        return redirect('factura-detalle',factura_u.id)    
    else:
        form=DetalleForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            'url_eliminar': url_eliminar,
            "detalles": detalles,
            "factura":factura_u,
            "detalle":detalle,       
        }
    return render(request, "factura\detalle-eliminar.html", context) 

def detalle_eliminar(request,pk):
    titulo_pagina='Marca'
    url_eliminar='/detalle-estado/'
    detalles= Detalle.objects.all()
    detalle= Detalle.objects.get(id=pk)
    accion_txt= f"la marca {detalle.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        detalle.delete()
        detalle_elemento= detalle.elemento
        messages.success(request,f'La marca {detalle_elemento} se eliminó correctamente!')
        return redirect('detalle_estado')
    else:
        form:DetalleForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "detalles": detalles,
            "url_eliminar": url_eliminar,       
        }
    return render(request, "factura/detalle-factura.html", context)
    
def factura_estado(request,pk, estado):
    titulo_pagina='Factura'
    tfacturas= Factura.objects.all()
    tfactura= Factura.objects.get(id=pk)
    eliminacion= Detalle.objects.filter(factura=tfactura)
    estado_msj=""
    estado_txt=""
    if estado == "Abierta":
        if not eliminacion.exists():
            estado_txt= "Eliminar"
            estado_msj= f"factura {tfactura.id}, una vez Eliminada ETC!"
            if request.method == 'POST':
                form = FacturaForm(request.POST)  
                tfactura.delete()
                messages.success(request,f'factura {pk} se eliminó correctamente!')
                return redirect('factura-tfactura')
            else:
                form=FacturaForm()
        else:
            print("la factura {pk} no se puede eliminar tiene elementos registrados!")
            messages.warning(request,f'la factura {pk} no se puede eliminar tiene elementos registrados!')
            return redirect('factura-tfactura')
    elif estado == "Cerrada":
        estado_txt= "Anular"
        estado_msj= f"factura {tfactura.id}, una vez Anulada ETC!"
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            Factura.objects.filter(id=pk).update(
                        estado='Anulada'
                    )
            tfactura_usuario=  tfactura.usuario
            messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
            return redirect('factura-tfactura')
        else:
            form=FacturaForm()
    else:
        estado_txt= "Cerrar"
        estado_msj= f"{estado_txt} la factura {tfactura.id}, una vez Cerrada ETC!"
        if request.method == 'POST':
            form = FacturaForm(request.POST)
            Factura.objects.filter(id=pk).update(
                        estado='Cerrada'
                    )
            tfactura_usuario=  tfactura.usuario
            messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
            return redirect('factura-tfactura')
        else:
            form:FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "estado_msj":estado_msj,
            "estado_txt":estado_txt,
            "tfacturas": tfacturas,     
    }
    return render(request, "factura/factura-estado.html", context)

def factura_anular(request,pk):
    titulo_pagina='Factura'
    tfacturas= Factura.objects.all()
    tfactura= Factura.objects.get(id=pk)
    accion_txt= f"factura {tfactura.id}, una vez anulada ETC!"
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        Factura.objects.filter(id=pk).update(
                    estado='Anulada'
                )
        tfactura_usuario=  tfactura.usuario
        messages.success(request,f'factura {tfactura.id} se anuló correctamente!')
        return redirect('factura-tfactura')                
    else:
        form:FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "tfacturas": tfacturas,
            "tfactura_usuario":tfactura_usuario,           
        }
    return render(request, "factura/factura-eliminar.html", context)