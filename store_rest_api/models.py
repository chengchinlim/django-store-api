from django.db import models


class Home(models.Model):
    message = models.CharField(max_length=100)


class Store(models.Model):
    class Meta:
        db_table = 'stores'
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
