from django.contrib.auth.models import User

from store_rest_api.models import Product
from store_rest_api.models.base import BaseModel
from django.db import models


class Store(BaseModel):
    class Meta:
        db_table = 'stores'
        app_label = 'store_rest_api'
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, related_name='+')

