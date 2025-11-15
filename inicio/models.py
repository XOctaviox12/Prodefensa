from django.db import models
from django.contrib.auth.models import User
from datetime import date

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

from django.utils.text import slugify

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)
    fecha_unica = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def fechas(self):
        if self.fecha_unica:
            return [self.fecha_unica]
        return [f.fecha for f in self.eventdate_set.all()]

    def es_pasado(self):
        from datetime import date
        return all(f < date.today() for f in self.fechas())

    def es_proximo(self):
        from datetime import date
        return any(f >= date.today() for f in self.fechas())

    def siguiente_fecha(self):
        from datetime import date
        fechas_futuras = [f for f in self.fechas() if f >= date.today()]
        return min(fechas_futuras) if fechas_futuras else None

    def __str__(self):
        return self.titulo
