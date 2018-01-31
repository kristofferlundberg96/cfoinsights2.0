# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20180128_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
