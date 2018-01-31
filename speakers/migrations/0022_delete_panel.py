# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0021_auto_20180130_0556'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Panel',
        ),
    ]
