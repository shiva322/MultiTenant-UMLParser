# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models

class Tenant(models.Model):
    tenant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'TENANT_DETAILS'

class Scores(models.Model):
    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)
    GRADE_OPTIONS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    #grade = models.CharField(max_length=1,choices=GRADE_OPTIONS,blank = True) 
    test_case = models.CharField(max_length=50,null=True)
    score_attribute1 = models.CharField(max_length=100,blank = True,null=True)
    score_attribute2 = models.CharField(max_length=100,blank = True,null=True)
    score_attribute3 = models.CharField(max_length=100,blank = True,null=True)
    score_attribute4 = models.CharField(max_length=100,blank = True,null=True)
    class Meta:
        managed = True
        db_table = 'TENANT_SCORES'


