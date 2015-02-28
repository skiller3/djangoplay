# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('asset_id', models.IntegerField()),
                ('symbol', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('constraint_type', models.CharField(max_length=200)),
                ('comparison', models.CharField(max_length=2)),
                ('value', models.FloatField()),
                ('asset', models.ForeignKey(to='constraints.Asset')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
