from django.contrib import admin

from employees.models import Employee, Team

# Register your models here.
admin.site.register(Team)
admin.site.register(Employee)