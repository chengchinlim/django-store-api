from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from store_rest_api.services.product import ProductService, ProductSerializer


class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer

    # @extend_schema(responses={200: StoreSerializer})
    # def get(self, request):
    #     stores = StoreService.find_by_user_id(request.user_id)
    #     serializer = StoreSerializer(stores, many=True)
    #     result = {'data': serializer.data}
    #     return JsonResponse(result)

    @extend_schema(responses={200: ProductSerializer})
    def create(self, request):
        saved_products = ProductService.create(request.data, request.user_id)
        serializer = ProductSerializer(saved_products, many=True)
        result = {'data': serializer.data}
        return JsonResponse(result)

