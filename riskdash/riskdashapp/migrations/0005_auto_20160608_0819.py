# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-08 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskdashapp', '0004_auto_20160607_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='impact_rating',
            name='value',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='likelihood_rating',
            name='value',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='res_likelihood_rating',
            name='value',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='risk',
            name='Score',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='risk',
            name='previous_score',
            field=models.IntegerField(default='0'),
        ),
    ]
