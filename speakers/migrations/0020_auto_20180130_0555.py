# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0019_auto_20180129_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='cv_list',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
