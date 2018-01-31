# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='slug',
            field=models.SlugField(unique=True, blank=True),
        ),
    ]
