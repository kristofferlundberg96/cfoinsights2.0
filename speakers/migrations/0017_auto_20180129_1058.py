# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0016_speaker_cv_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='cv_list',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
