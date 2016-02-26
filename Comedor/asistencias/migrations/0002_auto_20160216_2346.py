# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True)),
                ('turno', models.IntegerField(db_index=True, choices=[(1, 'Medio D\xeda'), (2, 'Noche')])),
                ('centro', models.ForeignKey(to='asistencias.Centro')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='incidencia',
            unique_together=set([('fecha', 'centro', 'turno')]),
        ),
    ]
