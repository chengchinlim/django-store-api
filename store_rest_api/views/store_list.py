from django.core import serializers as django_serializers
from django.http import HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from store_rest_api.services.store_service import StoreService, StoreSerializer


class StoreListView(ListCreateAPIView):
    serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        queried_data = StoreService.find_all()
        data = django_serializers.serialize('json', queried_data)
        return HttpResponse(data, content_type='application/json')

    @extend_schema(responses={200: StoreSerializer})
    def create(self, request):
        new_name = request.data.get('name')
        store = StoreService.create(name=new_name)
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')