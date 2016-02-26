# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dieta', models.IntegerField(db_index=True, choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido \xfarico'), (4, 'Dieta protecci\xf3n g\xe1strica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta protecci\xf3n biliar'), (8, 'Dieta hipocal\xf3rica'), (9, 'Dieta hipercalorica')])),
                ('presentacion', models.IntegerField(db_index=True, verbose_name='Presentaci\xf3n', choices=[(1, 'Entera'), (2, 'Machacada'), (3, 'Pasada')])),
                ('come', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Comedores',
            },
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField(blank=True)),
                ('turno', models.IntegerField(db_index=True, choices=[(1, 'Medio D\xeda'), (2, 'Noche')])),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('centro', models.ForeignKey(to='asistencias.Centro')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, db_index=True)),
                ('apellido_1', models.CharField(max_length=50, db_index=True)),
                ('apellido_2', models.CharField(max_length=50, null=True, db_index=True)),
                ('tipo', models.IntegerField(db_index=True, choices=[(1, 'Usuario'), (2, 'Profesional')])),
                ('dieta_default', models.IntegerField(db_index=True, verbose_name='Tipo de Dieta', choices=[(1, 'Dieta normal'), (2, 'Dieta colesterol'), (3, 'Dieta Acido \xfarico'), (4, 'Dieta protecci\xf3n g\xe1strica'), (5, 'Dieta hipertensi\xf3n'), (6, 'Dieta diabetes'), (7, 'Dieta protecci\xf3n biliar'), (8, 'Dieta hipocal\xf3rica'), (9, 'Dieta hipercalorica')])),
                ('presentacion_default', models.IntegerField(db_index=True, verbose_name='Presentaci\xf3n', choices=[(1, 'Entera'), (2, 'Machacada'), (3, 'Pasada')])),
                ('come_default', models.BooleanField(verbose_name='Marcar si Come')),
                ('direccion', models.CharField(max_length=150)),
                ('ciudad', models.CharField(max_length=150)),
                ('cp', models.CharField(max_length=5)),
                ('provincia', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=50)),
                ('centro', models.ForeignKey(to='asistencias.Centro')),
                ('comedor_default', models.ForeignKey(to='asistencias.Comedor', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='diario',
            name='asistentes',
            field=models.ManyToManyField(to='asistencias.Usuario', through='asistencias.asistencia'),
        ),
        migrations.AddField(
            model_name='diario',
            name='centro',
            field=models.ForeignKey(to='asistencias.Centro'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='comedor',
            field=models.ForeignKey(to='asistencias.Comedor'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='diario',
            field=models.ForeignKey(to='asistencias.Diario'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='usuario',
            field=models.ForeignKey(to='asistencias.Usuario'),
        ),
        migrations.AlterUniqueTogether(
            name='diario',
            unique_together=set([('fecha', 'centro', 'turno')]),
        ),
    ]
