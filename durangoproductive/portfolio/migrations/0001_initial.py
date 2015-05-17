# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=250, help_text='Briefly describe the asset. Limited to 250 characters.')),
                ('art', models.ImageField(upload_to='images/portfolio/assets', help_text='The art to associated with this project asset.')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, help_text='Limited to 250 characters')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, help_text='No HTML allowed')),
                ('description_html', models.TextField(blank=True, editable=False)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, help_text='Limited to 100 characters.')),
                ('slug', models.SlugField(help_text='Populates from the client name field automatically.')),
                ('description', models.TextField(help_text='No HTML allowed')),
                ('description_html', models.TextField(blank=True, editable=False)),
                ('lead_art', sorl.thumbnail.fields.ImageField(upload_to='images/portfolio/projects', help_text='Used for project representation on homepage and list view.')),
                ('is_featured', models.BooleanField(default=False, help_text='Determines whether the project will         be displayed on the homepage.')),
                ('is_public', models.BooleanField(default=True, help_text='Determines whether the project is public on         the website. Admins can view if false.')),
                ('completion_date', models.DateField(help_text='When was this project completed?')),
                ('categories', models.ManyToManyField(to='portfolio.Category')),
            ],
            options={
                'ordering': ('completion_date',),
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(to='portfolio.Project'),
        ),
    ]
