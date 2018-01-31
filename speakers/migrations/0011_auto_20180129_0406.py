# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

def give_slug(apps, schema_editor):
    Speaker = apps.get_model('speakers', 'Speaker')
    for speaker in Speaker.objects.all():
        speaker.slug = slugify(speaker.name)
        speaker.save()

class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0010_auto_20180129_0406'),
    ]

    operations = [
        migrations.RunPython(give_slug)
    ]
