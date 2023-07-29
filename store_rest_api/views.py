from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as django_serializers
from django.http import HttpResponse
from store_rest_api.models import Store, Home


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ['message']


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Modify the data here
        # data['field1'] = data['field1'].upper()
        return data


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

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request, store_id):
        store = Store.objects.get(pk=store_id)
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')

    @extend_schema(responses={200: StoreSerializer})
    def update(self, request, store_id):
        new_name = request.data.get('name')
        store = Store.objects.get(pk=store_id)
        store.name = new_name
        store.save()
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')
