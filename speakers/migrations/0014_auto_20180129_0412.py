# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

def give_slug(apps, schema_editor):
    Speaker = apps.get_model('speakers', 'Speaker')
    for speaker in Speaker.objects.all():
        name = speaker.name.lower()
        i18ized_name = name.replace('ø', "oe").replace("å", "aa").replace("æ", "ae")
        speaker.slug = slugify(i18ized_name)
        speaker.save()

class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0013_auto_20180129_0410'),
    ]

    operations = [
        migrations.RunPython(give_slug)
    ]
