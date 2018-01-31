# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0006_speaker_panels'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='title',
            field=models.TextField(default='CFO @ DFDS'),
            preserve_default=False,
        ),
    ]
