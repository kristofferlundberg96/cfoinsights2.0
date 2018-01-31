from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MembersView(TemplateView):
    template_name = "employees/member_list.html"

class MemberDetailView(TemplateView):
    template_name = "employees/member_details.html"