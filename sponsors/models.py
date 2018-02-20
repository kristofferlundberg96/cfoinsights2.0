from random import randint

from django.contrib import admin
from django.db.models.aggregates import Count
from django.db import models
from django import forms
from django.utils.text import slugify

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

# Create your models here.

CATEGORY_CHOICES = [
        (0, "Partners"),
        (1, "Network Partners"),
        (2, "Content Partners"),
        (3, "Media Partners"),
    ]


class SponsorManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def random_featured(self):
        count = self.filter(featured=True).aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.filter(featured=True)[random_index]


class Sponsor(models.Model):
    name = models.TextField()
    link = models.TextField()
    category = models.TextField()
    company_logo = models.ImageField(upload_to='sponsors/company_logos')
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = models.Manager()
    randoms = SponsorManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Sponsor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('category',)

class SponsorModelForm(forms.ModelForm):
    #description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Sponsor
        exclude = ('slug',)

class SponsorModelAdmin(admin.ModelAdmin):
    form = SponsorModelForm