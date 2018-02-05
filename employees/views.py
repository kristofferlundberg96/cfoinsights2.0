from django.shortcuts import render
from django.views.generic import DetailView, ListView

from employees.models import Employee

# Create your views here.
class MembersView(ListView):
    model = Employee
    context_object_name = "employees"
    template_name = "employees/member_list.html"
    ordering = ['name']

class MemberDetailView(DetailView):
    model = Employee
    context_object_name = "employee"
    template_name = "employees/member_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        context['name'] = context['employee'].name.split()[0]
        return context