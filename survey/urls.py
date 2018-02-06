from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.SurveyTemplateView.as_view(), name='survey'),
    url(r'about/$', views.SurveyAboutView.as_view(), name='about'),
    url(r'2018/$', views.SurveyQuestionsView.as_view(), name='questions'),
]