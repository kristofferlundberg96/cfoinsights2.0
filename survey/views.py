from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SurveyTemplateView(TemplateView):
    context_object_name = 'speakers_list'
    template_name = "speakers/speakers.html"
