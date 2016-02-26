# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django import forms

from models import *


class DiarioForm(forms.ModelForm):

    centro = forms.CharField( widget=forms.TextInput(attrs={'readonly': 'True'}))

    class Meta:
        model = Diario
        fields = '__all__'

    def clean_centro(self, *args, **kwargs):
        data = self.cleaned_data
        data['centro'] = Centro.objects.get(pk=data['centro'])
        return data['centro']


