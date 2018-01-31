# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_speaker_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='company',
            field=models.TextField(default='DFDS'),
            preserve_default=False,
        ),
    ]
