# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 22:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('networkinstitute', '0003_project_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=datetime.datetime(2016, 3, 8, 22, 51, 25, 297000, tzinfo=utc), max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, unique=True, default=None),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, unique=True, default=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(help_text='Please state the last date for applying to the project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Please provide a description, be sure to mention skills required, number of jobs available etc.'),
        ),
    ]
