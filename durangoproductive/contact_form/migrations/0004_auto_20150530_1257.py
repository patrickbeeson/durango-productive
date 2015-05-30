# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0003_communication_contacted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='contacted_date',
            field=models.DateTimeField(help_text='Date when this communication was marked as contacted.', null=True, blank=True),
        ),
    ]
