# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_auto_20150530_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='contacted_date',
            field=models.DateTimeField(help_text='Date when this communication was marked as contacted.', default=datetime.datetime(2015, 5, 30, 12, 53, 57, 385362), blank=True),
            preserve_default=False,
        ),
    ]
