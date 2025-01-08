from django.db import models


class EventConfig(models.Model):
    name = models.CharField(max_length=200)
    memo = models.CharField(max_length=200)


class Date(models.Model):
    day = models.DateField(max_length=200)
    # 予定の日


class CreatedDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # 予定作成日
