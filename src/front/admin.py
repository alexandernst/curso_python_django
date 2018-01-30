from django.contrib import admin

from .models import Persona, Mascota


class MasconaInline(admin.StackedInline):
    model = Mascota


class PersonaAdmin(admin.ModelAdmin):
    inlines = [MasconaInline]


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Mascota)
