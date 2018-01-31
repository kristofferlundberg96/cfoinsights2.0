# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_sponsor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
