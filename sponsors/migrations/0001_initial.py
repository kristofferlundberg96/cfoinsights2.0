# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('description', tinymce.models.HTMLField()),
                ('link', models.TextField()),
                ('category', models.TextField()),
                ('company_logo', models.ImageField(upload_to='sponsors/company_logos')),
            ],
        ),
    ]
