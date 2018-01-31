from django.shortcuts import render
from django.views.generic import ListView

from agenda.models import Panel

# Create your views here.
class AgendaView(ListView):
    template_name = "agenda/index.html"
    model = Panel
    context_object_name = 'panels'

    def get_queryset(self, **kwargs):
        panels = super(AgendaView, self).get_queryset(**kwargs)
        panel_categories = {}
        for panel in panels:
            if not panel.category in panel_categories:
                panel_categories[panel.category] = []
            panel_categories[panel.category].append(panel)

        for category in panel_categories:
            panel_categories[category] = list(zip("ABC", panel_categories[category]))

        return panel_categories