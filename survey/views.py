from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SurveyTemplateView(TemplateView):
    template_name = "survey/survey.html"

class SurveyAboutView(TemplateView):
    template_name = "survey/survey_about.html"

class SurveyQuestionsView(TemplateView):
    template_name = "survey/survey_questions.html"