from django.db import models


class Adress(models.Model):
    line_adress1 = models.CharField(max_length=150)
    line_adress2 = models.CharField(max_length=150,blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=70)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.line_adress1
    