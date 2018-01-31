from django.contrib import admin

from agenda.models import Panel, PanelModelAdmin

# Register your models here.
admin.site.register(Panel, PanelModelAdmin)