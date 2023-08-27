from django.core import serializers as django_serializers
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from store_rest_api.services.store import StoreService, StoreSerializer


class StoreListView(ListCreateAPIView):
    serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        stores = StoreService.find_by_user_id(request.user_id)
        serializer = StoreSerializer(stores, many=True)
        result = {'data': serializer.data}
        return JsonResponse(result)

    @extend_schema(responses={200: StoreSerializer})
    def create(self, request):
        new_name = request.data.get('name')
        store = StoreService.create(name=new_name)
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')