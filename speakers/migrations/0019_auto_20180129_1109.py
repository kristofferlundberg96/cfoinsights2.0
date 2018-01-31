# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0018_auto_20180129_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='bio',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
