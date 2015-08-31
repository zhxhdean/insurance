# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('p_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'insurance_category',
            },
        ),
    ]
