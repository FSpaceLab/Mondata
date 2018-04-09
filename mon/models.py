from django.db import models
from datetime import datetime

class Record(models.Model):
    volt = models.FloatField(null=True, blank=True)
    amper = models.FloatField(null=True, blank=True)
    watt = models.FloatField(null=True, blank=True)
    watt_hour = models.FloatField(null=True, blank=True)
    dt = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.dt)

