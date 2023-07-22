from django.urls import path
from store_rest_api import views

urlpatterns = [
    path('', views.home),
    path('stores/', views.stores),
]