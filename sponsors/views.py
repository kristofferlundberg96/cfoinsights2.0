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
            filtered_sponsors = sponsors.filter(category=n)

            if not filtered_sponsors:
                continue

            if filtered_sponsors.count() > 6:
                colw = 2
            else:
                colw = floor(12 / filtered_sponsors.count())

            label = categories[n]

            sponsors_by_category[label] = {
                'colw': colw,
                'sponsors': filtered_sponsors,
            }

        context['sponsors'] = sponsors_by_category
        return context