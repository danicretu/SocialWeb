# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 11:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('networkinstitute', '0012_auto_20160309_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectowner',
            name='id',
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='networkinstitute.ProjectOwner'),
        ),
        migrations.AlterField(
            model_name='projectowner',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='owner', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]