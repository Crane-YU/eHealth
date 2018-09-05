# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_design', '0008_auto_20180831_0021'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
