# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-20 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20181120_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='login_registration.Users'),
        ),
    ]