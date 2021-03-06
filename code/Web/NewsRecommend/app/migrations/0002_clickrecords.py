# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.DateTimeField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TNews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Users')),
            ],
        ),
    ]
