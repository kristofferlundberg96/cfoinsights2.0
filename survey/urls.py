from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.SurveyTemplateView.as_view(), name='survey'),
    url(r'about/$', views.SurveyAboutView.as_view(), name='about'),
    url(r'questions/$', views.SurveyQuestionsView.as_view(), name='questions'),
    url(r'ajax/submit$', views.survey_ajax_submit, name='submit_response'),
]