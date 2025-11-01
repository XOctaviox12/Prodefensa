from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Descuento, Actividad

# Vista principal del menú
def inicio(request):
    return render(request, 'inicio/inicio.html')
# Vistas de cada sección
def nosotros(request):
    return render(request, 'inicio/nosotros.html')

def comunidad(request):
    descuentos = Descuento.objects.all()
    return render(request, 'inicio/comunidad.html', {'descuentos': descuentos})

def servicios(request):
    actividades = Actividad.objects.all()
    return render(request, 'inicio/servicios.html',{'actividades':actividades})

def convenios(request):
    return render(request, 'inicio/convenios.html')

def unete(request):
    return render(request, 'inicio/unete.html')

def aviso_privacidad(request):
    return render(request, 'inicio/aviso_privacidad.html')


# tienda y carrito
def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'inicio/tienda.html', {'productos': productos})

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto.id) in carrito:
        carrito[str(producto.id)]['cantidad'] += 1
    else:
        carrito[str(producto.id)] = {'nombre': producto.nombre, 'precio': float(producto.precio), 'cantidad': 1}

    request.session['carrito'] = carrito
    return redirect('tienda')

def quitar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if str(producto_id) in carrito:
        del carrito[str(producto_id)]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'inicio/tienda/carrito.html', {'carrito': carrito, 'total': total})



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Correo o contraseña incorrectos')
    return render(request, 'inicio/login.html')


# Registro
def signup_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():
            messages.error(request, 'El correo ya está registrado')
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=nombre,
                last_name=apellido
            )
            login(request, user)
            return redirect('inicio')

    return render(request, 'inicio/signup.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('inicio')