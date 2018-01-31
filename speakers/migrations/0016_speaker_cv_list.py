# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('speakers', '0015_auto_20180129_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='cv_list',
            field=cms.models.fields.PlaceholderField(null=True, editable=False, to='cms.Placeholder', slotname='cv_list'),
        ),
    ]
