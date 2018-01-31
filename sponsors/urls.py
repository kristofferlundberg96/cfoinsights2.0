from django.conf.urls import include, url

from . import views

urlpatterns = [
    url('', views.SponsorsView.as_view(), name='sponsors'),
]