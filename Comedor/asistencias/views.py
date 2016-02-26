# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from models import *
import datetime


def get_string(p_iValue, p_lArray):
    for v,k in p_lArray:
        if v == p_iValue:
            return k
    return str(None)

def get_value(p_sValue, p_lArray):
    for v,k in p_lArray:
        if k == p_sValue:
            return v
    return None

def comidas_detail(request, p_iComedorId, p_iTurno):
    dInfo = {}
    text = u'<pre>'
    today = datetime.date.today()
    for oUser in asistencia.objects.filter(comedor_id = p_iComedorId,
                                       come = True,
                                       diario__turno= p_iTurno,
                                       diario__fecha__year=today.year,
                                       diario__fecha__month=today.month,
                                       diario__fecha__day=today.day):
        value = get_string(oUser.dieta, T_DIETA) + u' - ' + get_string(oUser.presentacion, T_PRESENTACION)
        if value in dInfo.keys():
            dInfo[value] += 1
        else:
            dInfo[value] = 1

    # hacer template bien...
    for k,v in dInfo.iteritems():
        text += k + u": " + unicode(v) + u"\n"
    text += "</pre>"

    sTurno = get_string(int(p_iTurno), T_TURNO)
    return HttpResponse(u"Comedor %s (%s)- %s <br/> %s" % (p_iComedorId, sTurno, str(today.strftime('   %d, %b %Y'))[2:], text))

def asistentes_detail(request, p_iComedorId, p_iTurno ):
    dInfo = {}
    text = u'<pre style="font-size: 20px;"><ul>'
    tPresentacionEntera = get_value('Entera', T_PRESENTACION)
    tDietaNormal = get_value('Dieta normal', T_DIETA)
    today = datetime.date.today()
    for oUser in asistencia.objects.filter(comedor_id = p_iComedorId,
                                       diario__turno= p_iTurno,
                                       diario__fecha__year=today.year,
                                       diario__fecha__month=today.month,
                                       diario__fecha__day=today.day).filter(
                                       Q(presentacion__gt=tPresentacionEntera) | Q(dieta__gt=tDietaNormal)
                                       ):
        # generacion
        sAsistente = oUser.usuario.nombre + " " + oUser.usuario.apellido_1 + " " + oUser.usuario.apellido_2
        sComida = get_string(oUser.dieta, T_DIETA) + u" - " + get_string(oUser.presentacion, T_PRESENTACION)
        # añadimos el texto - puedes meterlo en un td pero lo suyo en todo caso es que te mires los templates y hacerlo bien.
        text += "<li>" + sAsistente + u":\t\t " + sComida + "</li>"

    text += "</ul></pre>"
    sTurno = get_string(int(p_iTurno), T_TURNO)
    return HttpResponse(u"<span style='font-size: 35px;''>Comedor %s (%s)- %s </span><br/> %s" % (p_iComedorId, sTurno, str(today.strftime('   %d, %b %Y'))[2:], text))
