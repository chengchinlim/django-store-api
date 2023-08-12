from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as django_serializers
from django.http import HttpResponse, JsonResponse
from store_rest_api.services.store_service import StoreService, StoreSerializer
from store_rest_api.services.user_service import UserService, UserSerializer


class HomeView(APIView):

    @staticmethod
    def get(request):
        data = {'message': 'Hello from Django Store REST API!'}
        return Response(data)


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


class StoreView(RetrieveUpdateAPIView):
    serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        store = StoreService.find_by_id(request.user_id)
        serializer = StoreSerializer(store)
        return JsonResponse(serializer.data)

    @extend_schema(responses={200: StoreSerializer})
    def update(self, request, store_id):
        new_name = request.data.get('name')
        store = StoreService.find_by_id(store_id)
        store.name = new_name
        store.save()
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')


class UserView(RetrieveUpdateAPIView):
    def get(self, request, **kwargs):
        user = UserService.find_by_id(request.user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
