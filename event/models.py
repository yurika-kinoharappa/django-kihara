from django.db import models


class EventConfig(models.Model):
    name = models.CharField(max_length=200)
    # memo = models.CharField(max_length=200)
    # name = models.CharField(max_length=200)
