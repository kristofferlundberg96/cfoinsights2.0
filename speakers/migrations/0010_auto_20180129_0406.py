# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0009_speaker_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('category', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
