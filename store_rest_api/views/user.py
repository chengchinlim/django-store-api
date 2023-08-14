from django.http import JsonResponse
from store_rest_api.services.user_service import UserService, UserSerializer
from rest_framework.decorators import api_view


@api_view(['POST', 'GET'])
def user_view(request):
    if request.method == 'POST':
        return JsonResponse({'message': 'ok'})
    elif request.method == 'GET':
        user = UserService.find_by_id(request.user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
