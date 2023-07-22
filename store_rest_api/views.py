from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

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


class StoreView(APIView):
    # queryset = Store.objects.all()
    # serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        data = {'id': 1, 'name': 'Django Store'}
        return Response(data)
