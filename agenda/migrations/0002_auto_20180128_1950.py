# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='category',
            field=models.TextField(default=0, choices=[(0, 'Strategy'), (1, 'Financial Management'), (2, 'Future Trends')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panel',
            name='description',
            field=models.TextField(default='Get rich'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panel',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 28, 18, 49, 56, 978719, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='panel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 28, 18, 50, 0, 374896, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
