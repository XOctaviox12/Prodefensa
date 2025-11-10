from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('servicios/', views.servicios, name='servicios'),
    path('convenios/', views.convenios, name='convenios'),
    path('unete/', views.unete, name='unete'),
    path('aviso-privacidad/', views.aviso_privacidad, name='aviso_privacidad'),


    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),


    path('crear_sesion_checkout/', views.crear_sesion_checkout, name='crear_sesion_checkout'),
    path('crear_sesion_suscripcion/', views.crear_sesion_suscripcion, name='crear_sesion_suscripcion'), 
#     path('donacion-exitosa/', views.donacion_exitosa, name='donacion_exitosa'),
#     path('donacion-cancelada/', views.donacion_cancelada, name='donacion_cancelada'),

    path('historial-suscripciones/', views.historial_suscripciones, name='historial'),
    path('cancelar-suscripcion/', views.cancelar_suscripcion, name='cancelar_suscripcion'),
]
