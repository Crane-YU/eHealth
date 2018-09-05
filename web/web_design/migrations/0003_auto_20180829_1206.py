# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web_design', '0002_auto_20180827_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=datetime.datetime(2018, 8, 29, 12, 6, 34, 527355, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
