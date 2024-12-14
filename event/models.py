from django.db import models


class EventConfig(models.Model):
    name = models.CharField(max_length=200)
