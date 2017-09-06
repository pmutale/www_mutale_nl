# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-05 11:31
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stick2uganda', '0004_stick2ugandaplugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='stick2ugandaplugin',
            name='info',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stick2ugandaplugin',
            name='intro_small',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]