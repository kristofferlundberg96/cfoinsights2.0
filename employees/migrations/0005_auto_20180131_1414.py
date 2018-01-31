# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]
