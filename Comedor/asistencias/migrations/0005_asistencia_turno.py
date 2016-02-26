# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0004_auto_20160217_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='turno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
