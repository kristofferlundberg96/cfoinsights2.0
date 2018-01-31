# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

def push_bio_into_html(apps, schema_editor):
    Speaker = apps.get_model('speakers', 'Speaker')
    for speaker in Speaker.objects.all():
        speaker.bio_new = speaker.bio
        speaker.save()

class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0017_auto_20180129_1058'),
    ]

    operations = [
        migrations.RunPython(push_bio_into_html)
    ]
