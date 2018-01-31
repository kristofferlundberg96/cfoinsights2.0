from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.MembersView.as_view(), name='employees'),
    url(r'^(?P<slug>[-\w\d]+)', views.MemberDetailView.as_view(), name='employee_detail'),
]