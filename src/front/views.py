from django.views import generic
from django_filters.views import FilterView
from .filters import PersonaFilter
from .models import Persona


class IndexView(FilterView):  # generic.ListView
    filterset_class = PersonaFilter
    template_name = 'front/index.html'
    context_object_name = 'personas'
    paginate_by = 2


class DetailView(generic.DetailView):
    model = Persona
    template_name = 'front/detail.html'
