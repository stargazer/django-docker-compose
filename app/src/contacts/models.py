# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):

    names = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
