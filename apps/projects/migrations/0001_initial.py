# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-20 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Project', max_length=30)),
                ('description', models.TextField(default='Description here', null=True)),
                ('team_name', models.CharField(max_length=30)),
                ('team_code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compleation', models.IntegerField(default=0)),
                ('creativity', models.IntegerField(default=0)),
                ('collaberation', models.IntegerField(default=0)),
                ('complexity', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='login_registration.Users')),
            ],
        ),
    ]
