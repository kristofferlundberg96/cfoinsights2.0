import json

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from survey.models import ResponsesBeta

# Create your views here.
class SurveyTemplateView(TemplateView):
    template_name = "survey/survey_landing.html"

class SurveyAboutView(TemplateView):
    template_name = "survey/survey_about.html"

class SurveyQuestionsView(TemplateView):
    template_name = "survey/survey_questions.html"

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super(SurveyQuestionsView, self).get(request, *args, **kwargs)

def survey_ajax_submit(request):
    if request.is_ajax():
        json_data = json.dumps(request.POST)
        json_loaded = json.loads(json_data)
        ResponsesBeta.objects.create(data=json_loaded)
        return JsonResponse(request.POST)