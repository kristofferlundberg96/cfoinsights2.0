# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_auto_20180128_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='panels',
        ),
    ]
