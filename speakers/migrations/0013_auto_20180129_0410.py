# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.text import slugify

class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0012_auto_20180129_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]