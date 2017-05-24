# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_recommendset_read_ts'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaixinWebNews',
            fields=[
                ('news_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('topic', models.CharField(max_length=200)),
                ('img_href', models.CharField(max_length=200)),
            ],
        ),
    ]