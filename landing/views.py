from django.shortcuts import render

from django.views.generic import TemplateView

from speakers.models import Speaker
from sponsors.models import Sponsor
from agenda.models import Panel

# Create your views here.
class LandingView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        featured_speakers = []

        while len(featured_speakers) < 8:
            featured_speaker = Speaker.randoms.random_featured()
            if not featured_speaker in featured_speakers:
                featured_speakers.append(featured_speaker)

        featured_sponsors = Sponsor.objects.filter(featured=True)
        #while len(featured_sponsors) < 4:
        #    featured_sponsor = Sponsor.randoms.random_featured()
        #    if not featured_sponsor in featured_sponsors:
        #        featured_sponsors.append(featured_sponsor)

        context['featured_speakers'] = featured_speakers
        context['featured_sponsors'] = featured_sponsors
        context['strategy_panels'] = Panel.objects.filter(category=0)
        context['finance_panels'] = Panel.objects.filter(category=1)
        context['future_panels'] = Panel.objects.filter(category=2)
        return context