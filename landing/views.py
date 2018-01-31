from django.shortcuts import render

from django.views.generic import TemplateView

from speakers.models import Speaker

# Create your views here.
class LandingView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        featured_speakers = []

        while len(featured_speakers) < 4:
            featured_speaker = Speaker.randoms.random_featured()
            if not featured_speaker in featured_speakers:
                featured_speakers.append(featured_speaker)

        context['featured_speakers'] = featured_speakers
        return context