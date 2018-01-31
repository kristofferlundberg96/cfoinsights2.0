# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0011_auto_20180129_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
