from django.db import models

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
