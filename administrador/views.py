from datetime import datetime
from multiprocessing.reduction import ForkingPickler
from usuarios.Carrito import Carrito
from django.shortcuts import render, redirect
from administrador.forms import * 
from administrador.models import *
from django.contrib.auth.decorators import login_required
from gestion.decorators import unauthenticated_user, allowed_users
from django.contrib import messages 
from facturas.models import  Factura
from facturas.forms import  FacturaForm
from usuarios.models import  Usuario
from django.shortcuts import render, redirect
import os
from datetime import date
from usuarios.models import Usuario

@login_required(login_url="usuario-login")

def inicioadmin(request):
    titulo_pagina='Inicio Administrador'
    carrito = Carrito(request) 
    context={
        "carrito": carrito,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "administrador/inicioadmin.html", context)

def inicioadmin2(request,pk):
    titulo_pagina='inicio Administrador'
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


def tipoelemento(request):
    titulo_pagina="Categorias"
    categorias= Tipos_Elemento.objects.all()
    context={
        "categorias": categorias,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"administrador/categoria/categoria.html", context)

def ctipoelemento(request):
    titulo_pagina='Categorias'
    categorias= Tipos_Elemento.objects.all()
    if request.method == 'POST':
        form=TipoElementoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            categoria_nombre= form.cleaned_data.get('subcategoria')
            messages.success(request,f'La subcategoria {categoria_nombre} se agregó correctamente!')
            return redirect('administrador-elemento')
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
    return render(request, "administrador/categoria/categoria-crear.html", context)

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
    elemento = Elemento.objects.filter(estado = "Activo")
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
            "elemento": elemento
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
                    estado='Inactivo',
                    
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

def elemento_activar(request,pk):
    titulo_pagina='Elemento'
    url_eliminar= '/elemento/'
    elementos= Elemento.objects.all()
    elemento= Elemento.objects.get(id=pk)
    accion_txt= f"elemento {elemento.id}, una vez activado no hay marcha atras!"
    if request.method == 'POST':
        form = ElementoForm(request.POST)
        Elemento.objects.filter(id=pk).update(
                    estado='Activo'
                )
        elemento_nombre=  elemento.nombre
        messages.success(request,f'El usuario {elemento_nombre} se activó correctamente!')
        return redirect('administrador-elemento')                           
    else:
        form:ElementoForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "elementos": elementos,  
            "url_eliminar":url_eliminar 
    }
    return render(request, "administrador/elemento/elemento-activar.html", context)


def electrodomestico_favorito(request,pk):
    if Elemento.objects.get(id=pk).favorito:
        is_favorito=False
    else:
        is_favorito=True
    Elemento.objects.filter(id=pk).update(
        favorito=is_favorito
    )
    return redirect('administrador-elemento')

def marca(request):
    titulo_pagina="Marcas"
    marcas= Marca.objects.all()
    context={
        "marcas": marcas,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"administrador/marca/marca.html", context)

def marca_crear(request):
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
        return redirect('administrador-elemento')
    else:
        form= MarcaForm()
        context={
            "titulo_pagina": titulo_pagina,
            "marcas": marcas,
            "form": form,
        }
    return render(request,"administrador/marca/marca-crear.html", context)

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

def electrodomestico(request):
    titulo_pagina="Electrodomesticos"
    electrodomesticos= Electrodomestico.objects.all()
    context={
        "electrodomesticos": electrodomesticos,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"administrador/electrodomestico/electrodomestico.html", context)

def electrodomestico_crear(request):
    titulo_pagina='Electrodomesticos'
    electrodomesticos= Electrodomestico.objects.all()
    if request.method == 'POST':
        form= ElectrodomesticoForm(request.POST)
        if form.is_valid():
            form.save()
            electrodomestico_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El electrodomestico {electrodomestico_nombre} se agregó correctamente!')
            # insumo = form.cleaned_data('electrodomestico')
            # if insumo.estado != 'Activo':
            #     messages.success(request,'xd')
            # else:
            #     electrodomestico_nombre= form.cleaned_data.get('nombre')
            #     messages.success(request,f'El electrodomestico {electrodomestico_nombre} se agregó correctamente!')
            #     s =form.save()
            #     s.save()
        else:
            electrodomestico_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'Error al registrar el electrodomestico ¡Por favor verificar los datos!  ')    
        return redirect('administrador-servicio')
    else:
        form= ElectrodomesticoForm()  
        context={
            "titulo_pagina": titulo_pagina,
            "electrodomesticos": electrodomesticos,
            "form": form,
        }
    return render(request, "administrador/electrodomestico/electrodomestico-crear.html", context)

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
    electrodomestico = Electrodomestico.objects.filter(estado="Activo")
    titulo_pagina="Servicios"
    # usuarios = Usuario.objects.filter(usuario=Cliente)
    usuarios = Usuario.objects.filter(estado="Activo")
    items = Electrodomestico.objects.filter(estado = "Activo")
    servicios= Servicio.objects.all()
    if request.method == 'POST':
        form= ServicioForm(request.POST)
        if form.is_valid():
            aux= Servicio.objects.create(
            tiposervicio= request.POST['tiposervicio'],
            observacion= request.POST['observacion'],
            fallas_basicas= request.POST['fallas_basicas'],
            diagnostico= request.POST['diagnostico'],
            electrodomestico= Electrodomestico.objects.get(id= request.POST['electrodomestico']),
            usuario= Usuario.objects.get(Uid= request.POST['usuario']),
            )
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
            "form": form ,
            "usuario": usuarios,
            "item": items,
            "electrodomestico": electrodomestico,
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
            servicio_electrodomestico= form.cleaned_data.get('nombre')
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


def exportar_datos(request):
    date_now = date.today()
    tabla = request.POST['opcion']
    os.system(f"mysqldump --add-drop-table --column-statistics=0 --password=admin -u root db_licuadoraspulido --tables {tabla}> gestion/static/tablas/BKP_{tabla}_{date_now}.sql")
    print('imprimio la tabla ', tabla )
    print('-------------------------------------------------------Hecho')
     
    
def importar_datos(archivo, request):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LISTO PA´ IMPRIMIR')
    try:
        print('------------------------IMPORTAR')
        os.system(f"mysql --password=admin -u root db_licuadoraspulido < {archivo[1:]} ")
        messages.success(request,'su backup fue realizado correctamente')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><Salio')
    except Exception as err:
        messages.warning(request,f'error {err} ')
        print('error ', err)

def copiaseguridad(request,tipo):
    titulo_pagina='Copia Seguridad'
    carrito = Carrito(request) 
    ejemplo_dir = 'gestion/static/tablas/'
    with os.scandir(ejemplo_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
        
    ruta = 'gestion/static/backup'
    with os.scandir(ruta) as bases:
       bases = [base.name for base in bases if base.is_file()]
    print(ficheros)
    filtrado=[]
    copiaseguridad = Copiaseguridad.objects.all()
    if request.method == 'POST' and tipo== "U":
        # Fetching the form data  
        form = CopiaseguridadForm(request.POST, request.FILES)
        if form.is_valid():
            nombre= request.POST['nombre']
            archivo = request.FILES['archivo']
            insert = Copiaseguridad(nombre=nombre, archivo=archivo)
            insert.save() 
            importar_datos(insert.archivo.url, request)  
            insert = Copiaseguridad(nombre=nombre, archivo=archivo)
            insert.save()     
            return redirect('administrador-copiaseguridad','A')
        else:
            print( "Error al procesar el formulario")    
    elif request.method == 'POST' and tipo== "D":
        exportar_datos(request)
        return redirect('administrador-copiaseguridad','A')
    else:
        form = CopiaseguridadForm()
    context ={
        "ficheros":ficheros,
        'bases':bases,
        "titulo_pagina":titulo_pagina,
        "form":form,
        "copiaseguridad":copiaseguridad
    }
    return render(request, 'administrador/copiaseguridad.html',context) 