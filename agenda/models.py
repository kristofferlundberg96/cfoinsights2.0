from django.contrib import admin
from django.db import models
from django import forms

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


# Create your models here.
class Panel(models.Model):
    name = models.TextField()
    description = HTMLField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.TextField()

    def __str__(self):
        return self.name

class PanelModelForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    CATEGORY_CHOICES = [
        (0, "Strategy"),
        (1, "Financial Management"),
        (2, "Future Trends"),
        (3, "Keynote 1"),
        (4, "Keynote 2"),
        (5, "Keynote 3"),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

class PanelModelAdmin(admin.ModelAdmin):
    form = PanelModelForm