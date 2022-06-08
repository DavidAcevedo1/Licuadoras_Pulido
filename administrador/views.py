from dataclasses import field
from datetime import datetime
from django.shortcuts import render, redirect
from administrador.forms import  ElectrodomesticoEditarForm,StockForm, ElectrodomesticoForm, MarcaEditarForm, ServicioEditarForm, TipoElementoEditarForm, TipoElementoForm, UsuarioEditarForm, UsuarioForm, ElementoForm, ElementoEditarForm, FacturaEditarForm, FacturaForm, MarcaForm, ServicioForm
from administrador.models import Electrodomestico,Elemento, Factura, Marca, Servicio, Stock, Tipos_Elemento, Usuario
from django.contrib.auth.decorators import login_required
from gestion.decorators import unauthenticated_user, allowed_users
from django.contrib import messages 

@login_required(login_url="usuario-login")

def inicioadmin(request):
    titulo_pagina='Inicio Administrador'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "administrador/inicioadmin.html", context) 

def usuario(request):
    titulo_pagina='Usuarios'
    usuarios= Usuario.objects.all()
    if request.method == 'POST':
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El usuario {usuario_nombre} se agregó correctamente!')
        else:
            messages.error(request,f'Error al registrar el usuario ¡Por favor verificar los datos!  ')    
            
    else:
        form= UsuarioForm()
    context={
            "titulo_pagina": titulo_pagina,
            "usuarios": usuarios,
            "form": form
        }
    return render(request, "administrador/usuario/usuario.html", context)

def usuario_editar(request,pk):
    titulo_pagina='Usuarios'
    usuarios= Usuario.objects.all()
    usuario= Usuario.objects.get(id=pk)
    documento= usuario.documento
    url_editar="/usuario"
    if request.method == 'POST':
        form= UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El usuario {usuario_nombre} se editó correctamente!')
            return redirect('administrador-usuario')
        else:
            usuario_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el usuario {usuario_nombre}')    
    else:
        form= UsuarioEditarForm(instance=usuario)
    context={
            "titulo_pagina": titulo_pagina,
            "usuarios":usuarios,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/usuario/usuario-editar.html", context)

def usuario_eliminar(request,pk):
    titulo_pagina='Usuarios'
    url_eliminar= '/usuario/'
    usuarios= Usuario.objects.all()
    usuario= Usuario.objects.get(id=pk)
    accion_txt= f"Usuario {usuario.documento}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= UsuarioForm(request.POST)
        Usuario.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        usuario_nombre= usuario.nombre
        messages.success(request,f'El usuario {usuario_nombre} se eliminó correctamente!')
        return redirect('administrador-usuario')
    else:
        form= UsuarioForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "usuarios":usuarios,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/usuario/usuario-eliminar.html", context)

def tipoelemento(request):
    titulo_pagina='Categoria'
    categorias= Tipos_Elemento.objects.all()
    if request.method == 'POST':
        form=TipoElementoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            categoria_nombre= form.cleaned_data.get('subcategoria')
            messages.success(request,f'La subcategoria {categoria_nombre} se agregó correctamente!')
            return redirect('administrador-categoria')
        else:
           
            categoria_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'La subcategoria ya se encuentra agregada!')    
        
    else:
        form= TipoElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "categorias": categorias,
            "form": form,
        }
    return render(request, "administrador/categoria/categoria.html", context)

def tipoelemento_editar(request,pk):
    titulo_pagina='Categorias'
    categorias= Tipos_Elemento.objects.all()
    categoria= Tipos_Elemento.objects.get(id=pk)
    documento=f"{categoria.subcategoria} con el ID {pk}"
    url_editar="/categoria"
    if request.method == 'POST':
        form= TipoElementoEditarForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            categoria_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La categoria {categoria_nombre} se editó correctamente!')
            return redirect('administrador-categoria')
        else:
            categoria_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar la categoria {categoria_nombre}')    
    else:
        form= TipoElementoEditarForm(instance=categoria)
    context={
            "titulo_pagina": titulo_pagina,
            "categorias":categorias,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/categoria/categoria-editar.html", context)

def tipoelemento_eliminar(request,pk):
    titulo_pagina='Categorias'
    url_eliminar= '/categoria/'
    categorias= Tipos_Elemento.objects.all()
    categoria= Tipos_Elemento.objects.get(id=pk)
    accion_txt= f"La categoria {categoria.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= TipoElementoForm(request.POST)
        categoria_nombre= categoria.nombre
        messages.success(request,f'La categoria {categoria_nombre} se eliminó correctamente!')
        return redirect('administrador-categoria')
    else:
        form= TipoElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "categorias":categorias,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/categoria/categoria-eliminar.html", context)

def elemento(request):
    titulo_pagina='Elemento'
    elementos= Elemento.objects.all()
    if request.method == 'POST':
        form= ElementoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            elemento_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El elemento {elemento_nombre} se agregó correctamente!')
        else:
            elemento_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'El elemento ya se encuentra agregado!')    
        return redirect('administrador-elemento')
    else:
        form= ElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "elementos": elementos,
            "form": form,
        }
    return render(request, "administrador/elemento/elemento.html", context)

def elemento_editar(request,pk):
    titulo_pagina='Elementos'
    elementos= Elemento.objects.all()
    elemento= Elemento.objects.get(id=pk)
    documento=f"{elemento.nombre} con el ID {pk}"
    url_editar="/elemento"
    if request.method == 'POST':
        form= ElementoEditarForm(request.POST, instance=elemento, files=request.FILES)
        if form.is_valid():
            form.save()
            elemento_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El elemento {elemento_nombre} se editó correctamente!')
            return redirect('administrador-elemento')
        else:
            elemento_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el elemento {elemento_nombre}')    
    else:
        form= ElementoEditarForm(instance=elemento) 
    context={
            "titulo_pagina": titulo_pagina,
            "elementos":elementos,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,   
    }
    return render(request, "administrador/elemento/elemento-editar.html", context)
            
def elemento_eliminar(request,pk):
    titulo_pagina='elementos'
    url_eliminar= '/elemento/'
    elementos= Elemento.objects.all()
    elemento= Elemento.objects.get(id=pk)
    accion_txt= f"Elemento {elemento.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= ElementoForm(request.POST)
        Elemento.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        elemento_nombre= elemento.nombre
        messages.success(request,f'El elemento {elemento_nombre} se eliminó correctamente!')
        return redirect('administrador-elemento')
    else:
        form= ElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "elementos":elementos,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/elemento/elemento-eliminar.html", context)

def marca(request):
    titulo_pagina='Marcas'
    marcas= Marca.objects.all()
    if request.method == 'POST':
        form= MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            marca_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La marca {marca_nombre} se agregó correctamente!')
        else:
            marca_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'La marca ya se encuentra agregado!')    
        return redirect('administrador-marca')
    else:
        form= MarcaForm()
        context={
            "titulo_pagina": titulo_pagina,
            "marcas": marcas,
            "form": form
        }
    return render(request, "administrador/marca/marca.html", context)

def marca_editar(request,pk):
    titulo_pagina='Marcas'
    marcas= Marca.objects.all()
    marca= Marca.objects.get(id=pk)
    documento=f"{marca.nombre} con el ID {pk}"
    url_editar="/marca"
    if request.method == 'POST':
        form= MarcaEditarForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            marca_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'La marca {marca_nombre} se editó correctamente!')
            return redirect('administrador-marca')
        else:
            marca_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar la marca {marca_nombre}')    
    else:
        form= MarcaEditarForm(instance=marca)
    context={
            "titulo_pagina": titulo_pagina,
            "marcas":marcas,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/marca/marca-editar.html", context)

def marca_eliminar(request,pk):
    titulo_pagina='Marcas'
    url_eliminar= '/marca/'
    marcas= Marca.objects.all()
    marca= Marca.objects.get(id=pk)
    accion_txt= f"La marca {marca.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= MarcaForm(request.POST)
        Marca.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        marca_nombre= marca.nombre
        messages.success(request,f'La marca {marca_nombre} se eliminó correctamente!')
        return redirect('administrador-marca')
    else:
        form= MarcaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "marcas":marcas,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/marca/marca-eliminar.html", context)

def factura(request):
    titulo_pagina='Facturas'
    facturas= Factura.objects.all()
    if request.method == 'POST':
        form= FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            factura_elemento= form.cleaned_data.get('elemento')
            messages.success(request,f'La factura {factura_elemento} se agregó correctamente!')
        else:
            factura_elemento= form.cleaned_data.get('elemento')
            messages.error(request,f'La factura que ingreso ya se encuentra registrado!')     
        return redirect('administrador-factura')
    else:
        form= FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "facturas": facturas,
            "form": form
    }
    return render(request, "administrador/factura/factura.html", context)

def factura_editar(request,pk):
    titulo_pagina='Facturas'  
    facturas= Factura.objects.all()
    factura= Factura.objects.get(id=pk)
    documento=f"{factura.elemento} con el ID {pk}"
    url_editar="/factura"
    if request.method == 'POST':
        form= FacturaEditarForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            factura_elemento= form.cleaned_data.get('elemento')
            messages.success(request,f'La factura {factura_elemento} se editó correctamente!')
            return redirect('administrador-factura')
        else:
            factura_elemento= form.cleaned_data.get('elemento')
            messages.error(request,f'Error al modificar el factura {factura_elemento}')     
    else:
        form= FacturaEditarForm(instance=factura)
    context={
            "titulo_pagina": titulo_pagina,
            "facturas":facturas,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/factura/factura-editar.html", context)

def factura_eliminar(request,pk):
    titulo_pagina='Facturas'
    url_eliminar= '/factura/'
    facturas= Factura.objects.all()
    factura= Factura.objects.get(id=pk)
    accion_txt= f"La factura {factura.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= FacturaForm(request.POST)
        Factura.objects.filter(id=pk).update(
                    estado='Anulado'
                )
        factura_fecha= factura.fecha
        messages.success(request,f'La factura {factura_fecha} se eliminó correctamente!')
        return redirect('administrador-factura')
    else:
        form= FacturaForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "facturas":facturas,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/factura/factura-eliminar.html", context)

def electrodomestico(request):
    titulo_pagina='Electrodomestico'
    electrodomesticos= Electrodomestico.objects.all()
    if request.method == 'POST':
        form= ElectrodomesticoForm(request.POST)
        if form.is_valid():
            form.save()
            electrodomestico_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El electrodomestico {electrodomestico_nombre} se agregó correctamente!')
        else:
            messages.error(request,f'Error al registrar el electrodomestico ¡Por favor verificar los datos!  ')    
            return redirect('administrador-electrodomestico')
    else:
        form= ElectrodomesticoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "electrodomesticos": electrodomesticos,
            "form": form
    }
    return render(request, "administrador/electrodomestico/electrodomestico.html", context)

def electrodomestico_editar(request,pk):
    titulo_pagina='Electrodomesticos'  
    electrodomesticos= Electrodomestico.objects.all()
    electrodomestico= Electrodomestico.objects.get(id=pk)
    documento=f"{electrodomestico.nombre} con el ID {pk}"
    url_editar="/electrodomestico"
    if request.method == 'POST':
        form= ElectrodomesticoEditarForm(request.POST, instance=electrodomestico)
        if form.is_valid():
            form.save()
            electrodomestico_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El electrodomestico {electrodomestico_nombre} se editó correctamente!')
            return redirect('administrador-electrodomestico')
        else:
            electrodomestico_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el electrodomestico {electrodomestico_nombre}')     
    else:
        form= ElectrodomesticoEditarForm(instance=electrodomestico)
    context={
            "titulo_pagina": titulo_pagina,
            "electrodomesticos":electrodomesticos,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/electrodomestico/electrodomestico-editar.html", context)

def electrodomestico_eliminar(request,pk):
    titulo_pagina='electrodomesticos'
    url_eliminar= '/electrodomestico/'
    electrodomesticos= Electrodomestico.objects.all()
    electrodomestico= Electrodomestico.objects.get(id=pk)
    accion_txt= f"Electrodomestico {electrodomestico.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= ElectrodomesticoForm(request.POST)
        Electrodomestico.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        electrodomestico_nombre= electrodomestico.nombre
        messages.success(request,f'El electrodomestico {electrodomestico_nombre} se eliminó correctamente!')
        return redirect('administrador-electrodomestico')
    else:
        form= ElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "electrodomesticos":electrodomesticos,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/electrodomestico/electrodomestico-eliminar.html", context)

def servicio(request):
    titulo_pagina="Servicios"
    servicios= Servicio.objects.all()
    if request.method == 'POST':
        form= ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            servicio_electrodomestico= form.cleaned_data.get('electrodomestico')
            messages.success(request,f'El servicio {servicio_electrodomestico} se agregó correctamente!')
        else:
            messages.error(request,f'Error al registrar el servicio ¡Por favor verificar los datos!  ')    
            return redirect('administrador-servicio')
    else:
        form= ServicioForm()
    context={
            "titulo_pagina": titulo_pagina,
            "servicios":servicios,
            "form": form 
    }
    return render(request, "administrador/servicio/servicio.html",context)

def servicio_editar(request,pk):
    titulo_pagina='Servicios'
    servicios= Servicio.objects.all()
    servicio= Servicio.objects.get(id=pk)
    documento=f"{servicio.electrodomestico} con el ID {pk}"
    url_editar="/servicio"
    if request.method == 'POST':
        form= ServicioEditarForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            servicio_electrodomestico= form.cleaned_data.get('nombre')
            messages.success(request,f'El servicio {servicio_electrodomestico} se editó correctamente!')
            return redirect('administrador-servicio')
        else:
            servicio_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al modificar el servicio {servicio_electrodomestico}')    
    else:
        form= ServicioEditarForm(instance=servicio)
    context={
            "titulo_pagina": titulo_pagina,
            "servicios":servicios,
            "form": form,
            "documento":documento,
            "url_editar":url_editar,
    }
    return render(request, "administrador/servicio/servicio-editar.html", context)

def servicio_eliminar(request,pk):
    titulo_pagina='servicios'
    url_eliminar= '/servicio/'
    servicios= Servicio.objects.all()
    servicio= Servicio.objects.get(id=pk)
    accion_txt= f"Servicio {servicio.id}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form= ServicioForm(request.POST)
        Servicio.objects.filter(id=pk).update(
                    estado='Inactivo'
                )
        servicio_electrodomestico= servicio.electrodomestico
        messages.success(request,f'El servicio {servicio_electrodomestico} se eliminó correctamente!')
        return redirect('administrador-servicio')
    else:
        form= ElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "servicios":servicios,
            "form": form,
            "url_eliminar":url_eliminar
    }
    return render(request, "administrador/servicio/servicio-eliminar.html", context)

def copiaseguridad(request):
    titulo_pagina='Copia Seguridad'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "administrador/copiaseguridad.html", context)


def stock(request,pk):
    titulo_pagina="Stock"
    elemento= Elemento.objects.get(id=pk)
    stocks= Stock.objects.filter(elemento=pk)
    if request.method == 'POST':
        form= StockForm(request.POST)
        if form.is_valid():
            stock= Stock.objects.create(
                fecha=  datetime.now().strftime("%Y-%m-%d"),
                elemento= elemento,
                stock_agregada = form.cleaned_data.get('stock_stock'),
                stock_stock = elemento.stock_elemento + form.cleaned_data.get('stock_stock'),
                
            )
            Elemento.objects.filter(id=pk).update(
                stock_elemento= stock.stock_stock
            )
            stockck_id= form.cleaned_data.get('id')
            messages.success(request,f'El stock con el id {stockck_id} se agregó correctamente!')
        return redirect('elemento-stock', pk)
    else:

        form = StockForm()
    context={
        "titulo_pagina": titulo_pagina,
        "stocks": stocks,
        "form":form,
        "elemento":elemento
    }
    return render(request, "administrador/elemento/elemento-stock.html", context)



