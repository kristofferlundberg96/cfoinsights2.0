# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20180128_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='name',
            field=models.TextField(default='Best practices in PMI'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='panel',
            name='category',
            field=models.TextField(),
        ),
    ]
