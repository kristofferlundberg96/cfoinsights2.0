from django.shortcuts import render
from django.views.generic import ListView

from agenda.models import Panel, CATEGORY_CHOICES

# Create your views here.
class AgendaView(ListView):
    template_name = "agenda/index.html"
    model = Panel
    context_object_name = 'panels'

    def get_queryset(self, **kwargs):
        panels = super(AgendaView, self).get_queryset(**kwargs)
        category_choices_human = {
            0: 'strategy',
            1: 'finance',
            2: 'future',
            3: 'keynote1',
            4: 'keynote2',
            5: 'keynote3',
        }

        panel_categories = {
            'strategy': [],
            'finance': [],
            'future': [],
            'keynote1': [],
            'keynote2': [],
            'keynote3': [],
        }
        for panel in panels:
            panel_category = category_choices_human[int(panel.category)]
            panel_categories[panel_category].append(panel)

        return panel_categories