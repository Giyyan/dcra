# coding=utf-8
from django.db import models


class Worker(models.Model):
    hostname = models.CharField()

    class Meta:
        managed = False
