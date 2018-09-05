# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web_design', '0003_auto_20180829_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=2000, default='DEFAULT VALUE')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2018, 8, 29, 12, 33, 13, 226759, tzinfo=utc))),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
