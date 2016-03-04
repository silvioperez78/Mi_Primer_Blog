# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 3, 4, 18, 56, 28, 484142, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
