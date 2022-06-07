from django.shortcuts import render
from usuarios.Carrito import Carrito
def inicio(request):
    titulo_pagina='Inicio'
    carrito = Carrito(request) 
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "index.html", context)  

def password_reset(request):
    titulo_pagina='Inicio Sesión'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "password_reset", context)    

def password_reset_confirm(request):
    titulo_pagina='Inicio Sesión'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "recuperacion/password_reset_confirm.html", context)    

def password_reset_form(request):
    titulo_pagina='xd'
    context={
        "titulo_pagina": titulo_pagina,
    }
    return render(request, "recuperacion/password_reset_form.html", context) 