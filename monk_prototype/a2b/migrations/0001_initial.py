# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.CharField(max_length=16, unique=True, serialize=False, verbose_name=b'stop id (eg. BEST:1234)', primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'stop name')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True)),
            ],
            options={
                'verbose_name_plural': 'BEST stops',
            },
            bases=(models.Model,),
        ),
    ]
