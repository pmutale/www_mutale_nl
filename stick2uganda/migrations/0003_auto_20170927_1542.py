# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-27 13:42
from __future__ import unicode_literals

import ckeditor.fields
import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('filer', '0007_auto_20161016_1055'),
        ('stick2uganda', '0002_auto_20170907_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='S2UImagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='stick2uganda_s2uimageplugin', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
        migrations.AddField(
            model_name='question',
            name='add_findings_placeholder',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='add_findings', to='cms.Placeholder'),
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, max_length=128000, null=True, upload_to='media/project'),
        ),
        migrations.AlterField(
            model_name='question',
            name='findings',
            field=ckeditor.fields.RichTextField(blank=True, default='<p>Add Your Findings here<p><p>Identify Your Audience here<p><p>Add Your Findings Description here<p><p>Add Your Conclusion and Recommendations here<p>', help_text='Do not delete the tags <pre><code>&lt;p&gt; ... &lt;p&gt;</code></pre>', null=True),
        ),
    ]