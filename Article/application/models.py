# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    content = models.TextField()
    number_of_votes = models.IntegerField()

    def __unicode__(self):
		return self.title

    class Meta:
        ordering = ["number_of_votes"]		