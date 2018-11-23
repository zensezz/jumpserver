# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0009_auto_20180326_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='protocol',
            field=models.CharField(choices=[('ssh', 'ssh'), ('rdp', 'rdp')], default='ssh', max_length=8),
        ),
        migrations.AlterField(
            model_name='session',
            name='date_start',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Date start'),
        ),
    ]