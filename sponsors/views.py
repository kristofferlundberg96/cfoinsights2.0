from math import floor

from django.shortcuts import render
from django.views.generic import ListView

from sponsors.models import Sponsor, CATEGORY_CHOICES

# Create your views here.
class SponsorsView(ListView):
    model = Sponsor
    context_object_name = 'sponsors'
    template_name = "sponsors/sponsors.html"

    def get_context_data(self, **kwargs):
        context = super(SponsorsView, self).get_context_data(**kwargs)
        sponsors = context['sponsors']

        sponsors_by_category = {}
        categories = dict(CATEGORY_CHOICES)
        for n in categories:
            sponsors = sponsors.filter(category=n)
            if not sponsors:
                continue
            colw = floor(12 / sponsors.count())
            label = categories[n]

            sponsors_by_category[label] = {
                'colw': colw,
                'sponsors': sponsors,
            }

        context['sponsors'] = sponsors_by_category
        return context