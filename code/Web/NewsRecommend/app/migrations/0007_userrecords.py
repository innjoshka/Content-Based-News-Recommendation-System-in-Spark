# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170524_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_time', models.DateTimeField()),
                ('read_ts', models.IntegerField()),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CaixinNews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Users')),
            ],
        ),
    ]
