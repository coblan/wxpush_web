# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mac',
            name='mac',
            field=models.CharField(blank=True, max_length=100, verbose_name='mac'),
        ),
    ]
