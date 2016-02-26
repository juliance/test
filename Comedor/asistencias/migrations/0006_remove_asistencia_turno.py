# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0005_asistencia_turno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='turno',
        ),
    ]
