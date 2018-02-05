# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_sponsor_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='description',
        ),
    ]
