# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

T_DIETA = (
    (1, 'Dieta normal'),
    (2, 'Dieta colesterol'),
    (3, 'Dieta Acido urico'),
    (4, 'Dieta proteccion gastrica'),
    (5, 'Dieta hipertensión'),
    (6, 'Dieta diabetes'),
    (7, 'Dieta proteccion biliar'),
    (8, 'Dieta hipocalorica'),
    (9, 'Dieta hipercalorica'),
    (10, 'Dieta Astringente'),
    (11, 'Dieta Estrenimiento'),
    (12, 'Dieta Colesterol + Acido Urico'),
    (13, 'Dieta Colesterol + Diabetes'),
    (14, 'Dieta Colesterol + Diabetes + Hipocalorica'),
    (15, 'Dieta Intolerancia Legumbres'),
    (16, 'Dieta especial'),
    (17, 'Dieta Celiaca'),
    (18, 'Dieta Diabetes + Hipertension'),
    (19, 'Dieta Intolerancia Lactosa'),
    (20, 'Dieta Musulamana')
)

T_PRESENTACION = (
    (1, 'Entera'),
    (2, 'Machacada'),
    (3, 'Pasada'),
)

# int
T_USUARIO = (
    (1, 'Usuario'),
    (2, 'Profesional')
)

T_TURNO = (
    (1, 'Medio Día'),
    (2, 'Noche')
)

T_SEXO = (
    (1, 'Mujer'),
    (2, 'Varon')
)


# Create your models here.



class Centro(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.nombre
        #return u"%s %s" % ( self.id, self.nombre)


class Responsable(models.Model):
    user = models.OneToOneField(User)
    centro = models.ForeignKey(Centro)
    #centro = models.ManyToManyField(Centro)


class Comedor(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Comedores'

    def __unicode__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False, db_index=True)
    apellido_1 = models.CharField(max_length=50, null=False, db_index=True)
    apellido_2 = models.CharField(max_length=50, null=True, db_index=True)
    tipo = models.IntegerField(choices=T_USUARIO, blank=False, db_index=True)
    centro = models.ForeignKey(Centro, blank=False)
    comedor_default = models.ForeignKey(Comedor, blank=True)
    dieta_default = models.IntegerField('Tipo de Dieta', db_index=True, blank=False, choices=T_DIETA)
    presentacion_default = models.IntegerField('Presentación', db_index=True, blank=False, choices=T_PRESENTACION)
    come_default = models.BooleanField('Marcar si Come')
    direccion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=150)
    cp = models.CharField(max_length=5)
    provincia = models.CharField(max_length=150)
    dni = models.CharField(max_length=50)


    def __unicode__(self):
        return u"%s %s %s (%s)" % (self.apellido_1, self.apellido_2, self.nombre, self.tipo)

    class Meta:
        ordering = ('tipo', 'apellido_1',)

class Diario(models.Model):
    fecha = models.DateField()
    centro = models.ForeignKey(Centro)
    observaciones = models.TextField(blank=True)
    turno = models.IntegerField(choices=T_TURNO, blank=False, db_index=True)
    asistentes = models.ManyToManyField(Usuario, through='asistencia', through_fields=('diario', 'usuario'))

    class Meta:
        unique_together = ('fecha', 'centro', 'turno')

    def __unicode__(self):
        return u"%s %s" % ( self.fecha, self.centro )

class asistencia(models.Model):
    diario = models.ForeignKey(Diario)
    usuario = models.ForeignKey(Usuario)
    comedor = models.ForeignKey(Comedor, blank=False)
    dieta = models.IntegerField(db_index=True, null=False, choices=T_DIETA)
    presentacion = models.IntegerField('Presentación', db_index=True, blank=False, choices=T_PRESENTACION)
    come = models.BooleanField()

    
class incidencia(models.Model):
    fecha = models.DateField()
    centro = models.ForeignKey(Centro)
    observaciones = models.TextField(blank=True)
    turno = models.IntegerField(choices=T_TURNO, blank=False, db_index=True)

    class Meta:
        unique_together = ('fecha', 'centro', 'turno')

    def __unicode__(self):
        return u"%s %s" % ( self.fecha, self.centro )
