from django.db import models

# Create your models here.
class Movie(models.Model):
    rate=models.FloatField()
    mname=models.CharField(max_length=300)
    hero=models.CharField()
    heroine=models.CharField()