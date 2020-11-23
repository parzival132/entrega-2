from django.shortcuts import render, redirect
from scooterlineapp.forms import RegistrarForm


def inicio(request):
    return render(request, "inicio.html")


def producto(request):
    return render(request, "producto.html")

def nosotros(request):
    return render(request, "nosotros.html")  

def registrar_usuario(request):
    datos = {'form':RegistrarForm()}
    if request.method == 'POST':
        formulario= RegistrarForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save()
            return redirect('login')
        datos["form"]=formulario

    return render(request, "registrar_usuario.html", datos)

def redireccion(request):
    if request.user.is_staff:
        return redirect('/admin')
    else:
        return redirect('inicio')



  