from django.shortcuts import render

from django.views.generic import TemplateView

from speakers.models import Speaker
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

        context['featured_speakers'] = featured_speakers
        context['strategy_panels'] = Panel.objects.filter(category=0)
        context['finance_panels'] = Panel.objects.filter(category=1)
        context['future_panels'] = Panel.objects.filter(category=2)
        return context