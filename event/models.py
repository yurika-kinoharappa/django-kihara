from django.db import models


class EventConfig(models.Model):
    name = models.CharField(max_length=200)
    memo = models.CharField(max_length=200, null=True)


class Date(models.Model):
    day = models.DateField(max_length=200, null=False)
    # 予定の日
    time1 = models.TimeField(max_length=200, null=True)
    time2 = models.TimeField(max_length=200, null=True)
    # 予定の時間


class CreatedDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # 予定作成日
