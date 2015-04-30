# coding: utf-8

from django.db import models

class Engine(models.Model):
    model = models.ForeignKey('Manufacturer')
    volume = models.FloatField()
    cylinder = models.IntegerField()
    clapan = models.IntegerField()
    date = models.DateTimeField(auto_now=True, verbose_name=u'Дата Создания')
    author = models.CharField(max_length=255, verbose_name=u'Сборщик')
    def __unicode__(self):
        return u'%s %s %s' %(self.model, self.volume, self.cylinder)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Марка производителя')
    model = models.CharField(max_length=255, verbose_name='Название модели')
    def __unicode__(self):
        return u'%s %s' % (self.name, self.model)