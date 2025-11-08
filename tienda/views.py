import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Producto
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, CarritoItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def tienda(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'tienda/lista_producto.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Crear carrito si no existe
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Agregar producto o aumentar cantidad si ya existe
    item, created_item = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created_item:
        item.cantidad += 1
        item.save()

    return redirect('ver_carrito')  # Redirige a la página de carrito

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.all()
    total = carrito.total
    return render(request, 'tienda/carrito.html', {'items': items, 'total': total})

@require_POST
def actualizar_carrito_ajax(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    try:
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad < 1:
            item.delete()
            return JsonResponse({'success': True, 'eliminado': True})
        else:
            item.cantidad = cantidad
            item.save()
            return JsonResponse({
                'success': True,
                'cantidad': item.cantidad,
                'subtotal': float(item.subtotal),
            })
    except ValueError:
        return JsonResponse({'success': False, 'error': 'Cantidad inválida'})
    

def checkout(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = carrito.items.all()
    line_items = []

    for item in items:
        line_items.append({
            'price_data': {
                'currency': 'mxn',
                'product_data': {
                    'name': item.producto.nombre,
                },
                'unit_amount': int(item.producto.precio * 100),  # centavos
            },
            'quantity': item.cantidad,
        })

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/tienda/exito/'),
        cancel_url=request.build_absolute_uri('/tienda/carrito/'),
        billing_address_collection='auto',
        customer_email=request.user.email if request.user.email else None,
        automatic_tax={'enabled': False},
    )

    return redirect(session.url)

def exito(request):
    return render(request, 'tienda/exito.html')