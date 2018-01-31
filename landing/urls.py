from django.conf.urls import include, url

from . import views

urlpatterns = [
    url('', views.LandingView.as_view(), name='index'),
]