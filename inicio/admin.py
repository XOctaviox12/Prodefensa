from django.contrib import admin
from .models import Descuento, Actividad, Suscripcion

admin.site.site_header = "Panel de Administración - CIPOL"
admin.site.index_title = "Gestión de Suscripciones y Donaciones"
admin.site.site_title = "Administrador CIPOL"

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "tipo", "status", "created_at")
    list_filter = ("status", "tipo")
    search_fields = ("user__username", "stripe_subscription_id")
    ordering = ("-created_at",)