# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='First and last name', max_length=200)),
                ('email', models.EmailField(help_text='Will be validated to ensure proper formatting', max_length=254)),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact form submissions',
                'ordering': ('-sent',),
                'verbose_name': 'Contact form submission',
            },
        ),
    ]
