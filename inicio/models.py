from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Descuento(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='descuentos/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
    

class Actividad(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='actividades/')

    def __str__(self):
        return self.titulo
    
class Suscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50, choices=[("mensual", "Mensual"), ("única", "Única")])
    status = models.CharField(max_length=50, default="active")  # active, canceled
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.tipo} - {self.status}"
