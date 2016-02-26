# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencias', '0008_auto_20160224_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='dieta',
            field=models.IntegerField(db_index=True, choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido urico'), (4, 'Dieta proteccion gastrica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta proteccion biliar'), (8, 'Dieta hipocalorica'), (9, 'Dieta hipercalorica'), (10, 'Dieta Astringente'), (11, 'Dieta Estrenimiento'), (12, 'Dieta Colesterol + Acido Urico'), (13, 'Dieta Colesterol + Diabetes'), (14, 'Dieta Colesterol + Diabetes + Hipocalorica'), (15, 'Dieta Intolerancia Legumbres'), (16, 'Dieta especial')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dieta_default',
            field=models.IntegerField(db_index=True, verbose_name='Tipo de Dieta', choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido urico'), (4, 'Dieta proteccion gastrica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta proteccion biliar'), (8, 'Dieta hipocalorica'), (9, 'Dieta hipercalorica'), (10, 'Dieta Astringente'), (11, 'Dieta Estrenimiento'), (12, 'Dieta Colesterol + Acido Urico'), (13, 'Dieta Colesterol + Diabetes'), (14, 'Dieta Colesterol + Diabetes + Hipocalorica'), (15, 'Dieta Intolerancia Legumbres'), (16, 'Dieta especial')]),
        ),
    ]
