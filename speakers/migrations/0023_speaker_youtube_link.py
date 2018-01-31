# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0022_delete_panel'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='youtube_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
