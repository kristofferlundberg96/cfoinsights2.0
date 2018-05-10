from random import randint

from django.contrib import admin
from django.db import models
from django.db.models.aggregates import Count
from django import forms
from django.utils.text import slugify

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE

from agenda.models import Panel

# Create your models here.

class SpeakerManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def random_featured(self):
        count = self.filter(featured=True).aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.filter(featured=True)[random_index]


class Speaker(models.Model):
    name = models.TextField()
    title = models.TextField()
    company = models.TextField()
    facebook_link = models.TextField(null=True, blank=True)
    twitter_link = models.TextField(null=True, blank=True)
    linkedin_link = models.TextField(null=True, blank=True)
    youtube_link = models.TextField(null=True, blank=True)
    panels = models.ManyToManyField(Panel, related_name="speakers")
    photo = models.ImageField(upload_to='speakers')
    og_image = models.ImageField(upload_to='speakers_og', null=True, blank=True)
    company_logo = models.ImageField(upload_to='speakers/company_logos')
    cv_list = HTMLField(null=True, blank=True)
    bio = HTMLField()
    slug = models.SlugField(unique=True, blank=True)
    featured = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)

    objects = models.Manager()
    randoms = SpeakerManager()

    class Meta:
        ordering = ['-moderator']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(Speaker, self).save(*args, **kwargs)

class SpeakerModelForm(forms.ModelForm):
    cv_list = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    bio = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Speaker
        exclude = ('slug',)


class SpeakerModelAdmin(admin.ModelAdmin):
    form = SpeakerModelForm
