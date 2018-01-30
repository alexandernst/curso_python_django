import django_filters
from .models import Persona


class PersonaFilter(django_filters.FilterSet):
    class Meta:
        model = Persona
        fields = {
            'nombre': ['contains'],
            'fecha_nacimiento': ['year__gt']
        }
        order_by = ['pk']

    @property
    def qs(self):
        parent = super(PersonaFilter, self).qs
        # Filtrar por permisos del usuario actual
        # Filtrar solo personas activas
        # etc...
        return parent
