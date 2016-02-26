# -*- coding: utf-8 -*-

from django.conf.urls import url

import views

urlpatterns = [
    url(r'^comidas/(?P<p_iComedorId>[0-9]+)/(?P<p_iTurno>[0-9]+)/$', views.comidas_detail, name='comidas_detail'),
    url(r'^asistentes/(?P<p_iComedorId>[0-9]+)/(?P<p_iTurno>[0-9]+)/$', views.asistentes_detail, name='asistentes_detail'),
]
