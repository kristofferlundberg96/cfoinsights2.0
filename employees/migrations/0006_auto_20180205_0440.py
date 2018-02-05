# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20180131_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.TextField(default='Porcelænshaven 26'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.TextField(default='Copenhagen'),
            preserve_default=False,
        ),
    ]
