from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.SpeakersView.as_view(), name='speakers'),
    url(r'^(?P<slug>[-\w\d]+)', views.SpeakerDetailView.as_view(), name='speaker_detail'),
]