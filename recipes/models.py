# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=16)

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()

