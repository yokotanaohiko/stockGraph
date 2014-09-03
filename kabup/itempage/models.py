
#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Item(models.Model):
    meigara = models.CharField(u'始値',max_length=256)
    meigara_num = models.PositiveIntegerField(u'銘柄番号')
    hajimene = models.PositiveIntegerField(u'始値')
    owarine = models.PositiveIntegerField(u'終値')
    takane = models.PositiveIntegerField(u'高値')
    yasune = models.PositiveIntegerField(u'安値') 
    check_date = models.DateField(u'掲載開始日',null=True);
    
    def __unicode__(self):
        return self.item_code

    class Meta:
        db_table='kabuka'

class Meigara(models.Model):
    num = models.PositiveIntegerField()
    torihiki = models.CharField(max_length=256)
    meigara = models.CharField(max_length=256);

    def __unicode__(self):
        return self.name
    class Meta:
        db_table='meigara'
