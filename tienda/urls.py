from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('tienda/<int:producto_id>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/actualizar-ajax/<int:item_id>/', views.actualizar_carrito_ajax, name='actualizar_carrito_ajax'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('exito/', views.exito, name='exito'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
