from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Home(models.Model):
    message = models.CharField(max_length=100)


class Store(BaseModel):
    class Meta:
        db_table = 'stores'
    name = models.CharField(max_length=100)
