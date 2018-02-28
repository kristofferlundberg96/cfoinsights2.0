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
class Team(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.TextField()
    title = models.TextField()
    bio = models.TextField()
    team = models.ForeignKey(Team, related_name="members", on_delete=models.CASCADE)
    education = models.TextField()
    school = models.TextField()
    work = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    linkedin_link = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='members')
    email = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    address = models.TextField()
    city = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name.replace('ø', 'oe').replace('å', 'aa').replace('æ', 'ae'))

        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
