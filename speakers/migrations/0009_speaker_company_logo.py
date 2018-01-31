# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0008_speaker_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='company_logo',
            field=models.ImageField(default='none', upload_to='speakers/company_logos'),
            preserve_default=False,
        ),
    ]
