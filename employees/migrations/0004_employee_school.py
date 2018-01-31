# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20180131_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='school',
            field=models.TextField(default='Copenhagen Business School'),
            preserve_default=False,
        ),
    ]
