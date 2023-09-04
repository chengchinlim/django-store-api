from store_rest_api.models.base import BaseModel
from django.db import models


class Product(BaseModel):
    class Meta:
        db_table = 'products'
        app_label = 'store_rest_api'
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
