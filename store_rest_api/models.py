from django.db import models


class Home(models.Model):
    message = models.CharField(max_length=100)


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
