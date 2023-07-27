from django.db import models

# Create your models here.


class UsersApartments(models.Model):
    user = models.CharField(max_length=100)
    region = models.IntegerField()
    level = models.IntegerField()
    levels = models.IntegerField()
    rooms = models.IntegerField()
    area = models.FloatField()
    kitchen_area = models.FloatField()
    cost = models.IntegerField()
