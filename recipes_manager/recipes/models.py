# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ReceitasCaseiras(models.Model):
	nome = models.CharField(max_length=250)
	tipo = models.CharField(max_length=250)
