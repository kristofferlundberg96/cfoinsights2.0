# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0023_speaker_youtube_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
