# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-05 14:22
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stick2uganda', '0005_auto_20170905_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
