from django.shortcuts import render, redirect
from django.template import context
from facturas.models import Factura, Detalle
from facturas.forms import FacturaForm, DetalleForm
from django.contrib import messages 
from usuarios.models import Rol, Usuario

def factura(request):
    rol_c=Rol.objects.all()
    usuario_c=Usuario.objects.all()
    
    facturadb = Factura.objects.all()
    if request.method == 'POST':
        print(request.POST)
        form = FacturaForm(request.POST)
        
        if form.is_valid(): 
            aux= Factura.objects.create(
                rol_id= request.POST['rol'],
                usuario= Usuario.objects.get(Uid=request.POST['usuario']),
                tipofactura= form.cleaned_data.get('tipofactura'),
            )
            messages.success(request,f'!La factura se agregó correctamente!')
            return redirect('factura-detalle',aux.id)
    else:
        form = FacturaForm()
    context={
        'base_datos':facturadb,
        'form':form, 
        "rol":rol_c,
        "usuario":usuario_c
    }
    return render(request,'factura/crearFactura.html', context)

def tfactura(request):
    Rol_c=Rol.objects.all()
    Usuario_c=Usuario.objects.all()
    
    renew = '/factura/factura'
    tfacturas= Factura.objects.all()
    context={
        "tfacturas": tfacturas,
        "renew":renew,
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

def detalle(request,pk):
    titulo_pagina="facturas"
    detalles= Detalle.objects.filter(factura_id=pk)
    factura_u=Factura.objects.get(id=pk)

    if request.method == 'POST':
        form= DetalleForm(request.POST)
        if form.is_valid():
            
            factura= Detalle.objects.create(
                cantidad=form.cleaned_data.get('cantidad'),
                producto= form.cleaned_data.get('producto'),
                factura=factura_u,
                
            )
            producto= form.cleaned_data.get('Producto')
            messages.success(request,f' se agregó {producto} al la factura correctamente!')
            return redirect('factura-detalle', pk=pk)
    else:
        form= DetalleForm()
    context={
        "titulo_pagina": titulo_pagina,
        "detalles": detalles,
        "form":form,
        "factura":factura_u
    }
    return render(request, "factura/detalle-factura.html", context)

def detalle_estado(request,pk ):
    titulo_pagina='producto'
    u_detalles= Detalle.objects.get(id=pk)
    factura_u= u_detalles.factura
    detalles= Detalle.objects.filter(factura_id=factura_u.id)
    accion_txt= f"Eliminando detalle {u_detalles.id}, una vez eliminado no hay marcha atras!"
   
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
            "detalles": detalles,
            "factura":factura_u,
            "form":form,
        
            
    }
    return render(request, "factura/detalle-eliminar.html", context) 

def detalle_eliminar(request,pk):
    titulo_pagina='Marca'
    detalles= Detalle.objects.all()
    detalle= Detalle.objects.get(id=pk)
    accion_txt= f"la marca {detalle.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        detalle.delete()
        detalle_producto= detalle.producto
        messages.success(request,f'La marca {detalle_producto} se eliminó correctamente!')
        return redirect('detalle_estado')
                
    else:
        form:DetalleForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "detalles": detalles,
            
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
            messages.warning(request,f'la factura {pk} no se puede eliminar tiene productos registrados!')
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
           
    }
    return render(request, "factura/factura-eliminar.html", context)



# Create your views here.
