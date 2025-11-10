from django.contrib import admin
from .models import Descuento, Actividad, Suscripcion


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