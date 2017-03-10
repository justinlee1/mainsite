# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-16 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentalhealth', '0004_auto_20161216_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='ethnicity',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Ethnicity'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='gender',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Gender'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='identity',
            field=models.ManyToManyField(blank=True, to='mentalhealth.Identity'),
        ),
        migrations.AlterField(
            model_name='mentalhealthreview',
            name='sexual_orientation',
            field=models.ManyToManyField(blank=True, to='mentalhealth.SexualOrientation'),
        ),
    ]