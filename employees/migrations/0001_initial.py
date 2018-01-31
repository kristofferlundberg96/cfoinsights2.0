# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('bio', models.TextField()),
                ('education', models.TextField()),
                ('work', models.TextField()),
                ('slug', models.SlugField(unique=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(related_name='members', to='employees.Team'),
        ),
    ]
