from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as django_serializers
from django.http import HttpResponse, JsonResponse
from store_rest_api.models.store import Store
from store_rest_api.services.store_service import StoreService
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

    def to_representation(self, instance):
        data = super(UserSerializer, self).to_representation(instance)
        formatted = {
            'item': data
        }
        return formatted


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

    @staticmethod
    def get(request):
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


class UserAuthenticationView(ListCreateAPIView):
    def create(self, request, **kwargs):
        username = request.data.get('username')
        user = authenticate(username=username, password=request.data.get('password'))
        if user is not None:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({'message': 'Not authenticated'}, status=401)
