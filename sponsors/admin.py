from django.contrib import admin

from sponsors.models import Sponsor, SponsorModelAdmin

# Register your models here.
admin.site.register(Sponsor, SponsorModelAdmin)