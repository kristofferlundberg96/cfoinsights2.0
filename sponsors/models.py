from django.contrib import admin
from django.db import models
from django import forms
from django.utils.text import slugify

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

# Create your models here.

CATEGORY_CHOICES = [
        (0, "Gold"),
        (1, "Silver"),
        (2, "Bronze"),
        (3, "Roundtable Partners"),
        (4, "Partners"),
    ]

class Sponsor(models.Model):
    name = models.TextField()
    description = HTMLField()
    link = models.TextField()
    category = models.TextField()
    company_logo = models.ImageField(upload_to='sponsors/company_logos')
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Sponsor, self).save(*args, **kwargs)

class SponsorModelForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Sponsor
        exclude = ('slug',)

class SponsorModelAdmin(admin.ModelAdmin):
    form = SponsorModelForm