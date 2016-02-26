# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0003_auto_20160217_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsable',
            name='centro',
        ),
        migrations.AddField(
            model_name='responsable',
            name='centro',
            field=models.ForeignKey(default=1, to='asistencias.Centro'),
            preserve_default=False,
        ),
    ]
