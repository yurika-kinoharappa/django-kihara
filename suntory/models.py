from django.db import models

# Create your models here.


class santori(models.Model):
    text = models.CharField(max_length=1000)
    ganba = models.IntegerField(default=0)
    daijobu = models.IntegerField(default=0)
    aruaru = models.IntegerField(default=0)
