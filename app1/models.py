# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    refer   =  models.CharField(max_length=500)
#    active  = models.BooleanField(default=False)
