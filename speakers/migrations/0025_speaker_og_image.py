# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0024_speaker_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='og_image',
            field=models.ImageField(blank=True, null=True, upload_to='speakers_og'),
        ),
    ]
