# coding: utf-8
from avto import models
from django import forms

class EngineCharacteristics(forms.Form):
    model =forms.ModelChoiceField(queryset=models.Manufacturer.objects.all())
    volume = forms.FloatField()
    cylinder = forms.IntegerField()
    clapan = forms.IntegerField()
    author = forms.CharField()