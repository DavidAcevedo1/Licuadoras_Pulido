from django.shortcuts import render, redirect
from django.contrib import messages
from administrador.views import tipoelemento
from usuarios.forms import    ClienteForm, ProveedorForm, UsuarioForm
from usuarios.models import  Cliente, Proveedor, Usuario
from usuarios.Carrito import Carrito
from administrador.models import Elemento, Tipos_Elemento

def inicio(request):
    titulo_pagina='Inicio'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "index.html", context)

def cusuario(request):
    titulo_pagina="usuario"
    usuario_db = Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('Unombre')
            messages.success(request,f'El usuario {usuario_nombre} se agregó correctamente!')
            return redirect('usuario-crearUsuario')
    else:
        form = UsuarioForm()
    context={
        "titulo_pagina": titulo_pagina,
        "usuario_db": usuario_db,
        "form":form
    }
    return render(request,'usuarios/crearUsuario.html', context)

def tusuario(request):
    titulo_pagina="usuario"
    tusuarios= Usuario.objects.all()
    context={
        "tusuarios": tusuarios,
        "titulo_pagina":titulo_pagina
    }
    return render(request, "usuarios/tablaUsuario.html",context)

def vusuario (request,pk):
    titulo_pagina="Producto"
    usuario= Usuario.objects.get(Uid=pk) 
    print(usuario)
    context={
        "usuario": usuario,
        "titulo_pagina":titulo_pagina
    }
    return render(request,"usuarios/verusuario.html", context)

def usuario_crear(request):
    titulo_pagina="usuario"
    carrito = Carrito(request) 
    usuario_db = Usuario.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario_nombre= form.cleaned_data.get('Unombre')
            messages.success(request,f'El usuario {usuario_nombre} se agregó correctamente!')
            return redirect('usuario-crear')
    else:
        form = UsuarioForm()
    context={
        "titulo_pagina": titulo_pagina,
        "usuario_db": usuario_db,
        "form":form
    }
    return render(request,'usuarios/usuario-crear.html', context)

def Editarusuario(request,pk):
    titulo_pagina="Producto"
    tusuarios= Usuario.objects.get(id=pk)
    if request.method == 'POST':
        form= UsuarioForm(request.POST, instance=tusuarios)
        if form.is_valid():
            form.save()
        return redirect('usuario-tablaUsuario')
    else:
        form= UsuarioForm(instance=tusuarios)
        
        context={
        "tusuarios": tusuarios,
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "usuarios/editarusuario.html", ({'base_datos':tusuarios,'form':form,  "titulo_pagina":titulo_pagina}))

def usuario_eliminar(request,pk):
    titulo_pagina='Usuarios'
    tusuarios= Usuario.objects.all()
    tusuario= Usuario.objects.get(Uid=pk)
    accion_txt= f"usuario {tusuario.Uid}, una vez eliminado no hay marcha atras!"
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        Usuario.objects.filter(Uid=pk).update(
                    estado='Inactivo'
                )
        tusuario_nombre=  tusuario.Unombre
        messages.success(request,f'El usuario {tusuario_nombre} se eliminó correctamente!')
        return redirect('usuario-tablaUsuario')
                                   
    else:
        form:UsuarioForm()
    context={
            "titulo_pagina": titulo_pagina,
            "accion_txt":accion_txt,
            "tusuarios": tusuarios,
           
    }
    return render(request, "usuarios/usuario-eliminar.html", context)

def proveedor(request):
    titulo_pagina="Proveedores"
    proveedores= Proveedor.objects.all()
    context={
        "proveedores":proveedores,
        "titulo_pagina":titulo_pagina
    }
    return render(request, "proveedores/proveedores.html",context)


def proveedor_crear(request):
    titulo_pagina='Proveedor'
    proveedor= Proveedor.objects.all()
    if request.method == 'POST':
        form= ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            proveedor_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El proveedor {proveedor_nombre} se agregó correctamente!')
        else:
            proveedor_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'El proveedor ya se encuentra agregado!')    
        return redirect('usuario-proveedor')
    else:
        form= ProveedorForm()
    context={
            "titulo_pagina": titulo_pagina,
            "proveedor": proveedor,
            "form": form,
        }
    return render(request, "proveedores/crear-proveedor.html", context)

def proveedor_editar(request,pk):
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
            
def proveedor_eliminar(request,pk):
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

def cliente(request):
    titulo_pagina="Clientes"
    clientes= Cliente.objects.all()
    context={
        "clientes":clientes,
        "titulo_pagina":titulo_pagina
    }
    return render(request, "clientes/clientes.html",context)


def cliente_crear(request):
    titulo_pagina='Crear-Cliente'
    cliente= Cliente.objects.all()
    if request.method == 'POST':
        form= ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cliente_nombre= form.cleaned_data.get('nombre')
            messages.success(request,f'El cliente {cliente_nombre} se agregó correctamente!')
        else:
            cliente_nombre= form.cleaned_data.get('nombre')
            messages.error(request,f'El cliente ya se encuentra agregado!')    
        return redirect('usuario-cliente')
    else:
        form= ClienteForm()
    context={
            "titulo_pagina": titulo_pagina,
            "cliente": cliente,
            "form": form,
        }
    return render(request, "clientes/crear-cliente.html", context)


def restablecercontraseña(request):
    titulo_pagina='Restablecer Contraseña'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/restablecercontraseña.html", context)

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
    subcategorias= Tipos_Elemento.objects.filter(categoria="Productos")
    elementos = Elemento.objects.filter(tipo_elemento__categoria="Productos")
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
        "subcategorias":subcategorias,
    }
    return render(request, "usuarios/productos.html", context)

def serviciocliente(request):
    titulo_pagina='Servicios Cliente'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/servicioscliente.html", context)

def nosotros(request):
    titulo_pagina='Nosotros'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/nosotros.html", context)

def politicasprivacidad(request):
    titulo_pagina='Politicas de Privacidad'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
    }
    return render(request, "usuarios/politicasprivacidad.html", context) 
    
def carrito(request):
    titulo_pagina='Carrito'
    elementos = Elemento.objects.all()
    context={
        "titulo_pagina": titulo_pagina,
        "elementos":elementos,
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