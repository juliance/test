# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0006_remove_asistencia_turno'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ('tipo', 'apellido_1')},
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='dieta',
            field=models.IntegerField(db_index=True, choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido \xfarico'), (4, 'Dieta protecci\xf3n g\xe1strica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta protecci\xf3n biliar'), (8, 'Dieta hipocal\xf3rica'), (9, 'Dieta hipercalorica'), (10, 'Dieta especial')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dieta_default',
            field=models.IntegerField(db_index=True, verbose_name='Tipo de Dieta', choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido \xfarico'), (4, 'Dieta protecci\xf3n g\xe1strica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta protecci\xf3n biliar'), (8, 'Dieta hipocal\xf3rica'), (9, 'Dieta hipercalorica'), (10, 'Dieta especial')]),
        ),
    ]
