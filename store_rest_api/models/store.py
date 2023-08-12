from store_rest_api.models.base import BaseModel
from django.db import models


class Store(BaseModel):
    class Meta:
        db_table = 'stores'
        app_label = 'store_rest_api'
    name = models.CharField(max_length=100)