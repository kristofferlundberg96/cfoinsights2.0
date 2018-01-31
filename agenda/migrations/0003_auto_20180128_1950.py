# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20180128_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='panel',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
