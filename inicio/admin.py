from django.contrib import admin
from .models import Descuento, Actividad, Suscripcion, Evento, EventDate

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

class EventDateInline(admin.TabularInline):
    model = EventDate
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    inlines = [EventDateInline]
    list_display = ('titulo', 'fecha_unica', 'siguiente_fecha', 'es_proximo')
