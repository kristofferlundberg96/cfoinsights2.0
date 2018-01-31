# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20180128_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='facebook_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='linkedin_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='twitter_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
