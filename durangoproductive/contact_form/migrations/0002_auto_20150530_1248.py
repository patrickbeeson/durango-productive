# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='contacted',
            field=models.BooleanField(default=False, help_text='Indicates whether the sender has been contacted in response to their message.'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='communication',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
