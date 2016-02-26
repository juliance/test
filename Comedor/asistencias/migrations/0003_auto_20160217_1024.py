# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0002_auto_20160216_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsable',
            name='centro',
        ),
        migrations.AddField(
            model_name='responsable',
            name='centro',
            field=models.ManyToManyField(to='asistencias.Centro'),
        ),
    ]
