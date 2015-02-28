from django.db import models

class Asset(models.Model):
    timestamp = models.DateTimeField("timestamp")
    symbol = models.CharField(max_length=32)
    name = models.CharField(max_length=200)

    def isIBM(self):
        return self.symbol == "IBM"

class Constraint(models.Model):
    timestamp = models.DateTimeField("timestamp")
    constraint_type = models.CharField(max_length=200)
    asset = models.ForeignKey(Asset)
    comparison = models.CharField(max_length=2)
    value = models.FloatField()

