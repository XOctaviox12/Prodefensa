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
]
