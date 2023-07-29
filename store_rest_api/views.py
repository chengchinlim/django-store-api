from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as django_serializers
from django.http import HttpResponse, JsonResponse
from store_rest_api.models import Store, Home
from store_rest_api.services import StoreService


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ['message']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super(StoreSerializer, self).to_representation(instance)
        formatted = {
            'item': data
        }
        return formatted

class HomeView(APIView):
    # queryset = Home.objects.all()
    # serializer_class = HomeSerializer

    def get(self, request):
        data = {'message': 'Hello from Django Store REST API!'}
        return Response(data)


class StoreListView(ListCreateAPIView):
    serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        queried_data = Store.objects.all()
        data = django_serializers.serialize('json', queried_data)
        return HttpResponse(data, content_type='application/json')

    @extend_schema(responses={200: StoreSerializer})
    def create(self, request):
        new_name = request.data.get('name')
        store = Store.objects.create(name=new_name)
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')


class StoreView(RetrieveUpdateAPIView):
    serializer_class = StoreSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.store_service = StoreService()

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request, store_id):
        store = self.store_service.find_by_id(store_id)
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data)

    @extend_schema(responses={200: StoreSerializer})
    def update(self, request, store_id):
        new_name = request.data.get('name')
        store = Store.objects.get(pk=store_id)
        store.name = new_name
        store.save()
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')
