from django.shortcuts import render
from django.views.generic import ListView, DetailView

from agenda.models import Panel

from speakers.models import Speaker

# Create your views here.
class SpeakersView(ListView):
    model = Speaker
    context_object_name = 'speakers_list'
    template_name = "speakers/speakers.html"

class SpeakerDetailView(DetailView):
    model = Speaker
    context_object_name = "speaker"
    template_name = "speakers/speaker_detail.html"

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        context['first_name'] = context['speaker'].name.split()[0]

        speakers_to_recommend = []
        speaker = context['speaker']
        for panel in speaker.panels.all():
            for fellow_panelist in panel.speakers.all():
                if not speaker.name == fellow_panelist.name:
                    speakers_to_recommend.append(fellow_panelist)

            for same_category_panel in Panel.objects.filter(category=panel.category):
                if same_category_panel == panel:
                    continue
                for same_cat_speaker in same_category_panel.speakers.all():
                    speakers_to_recommend.append(same_cat_speaker)


        while not len(speakers_to_recommend) == 24:
            random_speaker = Speaker.randoms.random()

            if not random_speaker in speakers_to_recommend and random_speaker.name != speaker.name:
                speakers_to_recommend.append(random_speaker)

        recommendations = []
        for i in range(0, len(speakers_to_recommend), 6):
            recommendations.append(speakers_to_recommend[i:i + 6])


        context['recommendations'] = recommendations
        return context
