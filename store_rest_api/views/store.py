from django.core import serializers as django_serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView
from store_rest_api.services.store import StoreService, StoreSerializer


class StoreView(RetrieveUpdateAPIView):
    serializer_class = StoreSerializer

    @extend_schema(responses={200: StoreSerializer})
    def get(self, request):
        store_id = request.GET.get('store_id')
        try:
            store = StoreService.find_one(request.user_id, store_id)
        except ObjectDoesNotExist:
            return JsonResponse({'errors': {
                'dev': f'Store {store_id} not found',
                'user': f'Store {store_id} not found'
            }}, status=404)
        serializer = StoreSerializer(store)
        result = {'data': serializer.data}
        return JsonResponse(result)

    @extend_schema(responses={200: StoreSerializer})
    def update(self, request, store_id):
        new_name = request.data.get('name')
        store = StoreService.find_one(request.user_id, store_id)
        store.name = new_name
        store.save()
        data = django_serializers.serialize('json', [store])
        return HttpResponse(data, content_type='application/json')