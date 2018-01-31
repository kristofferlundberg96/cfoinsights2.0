from django.contrib import admin

from speakers.models import Speaker, SpeakerModelAdmin

# Register your models here.
admin.site.register(Speaker, SpeakerModelAdmin)