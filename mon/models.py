from django.db import models
from django.utils import timezone

class Record(models.Model):
    volt = models.FloatField(default=0, null=True, blank=True)
    amper = models.FloatField(default=0, null=True, blank=True)
    watt = models.FloatField(default=0, null=True, blank=True)
    watt_hour = models.FloatField(default=0, null=True, blank=True)
    dt = models.DateTimeField(default=timezone.now)

    comment = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.id)

