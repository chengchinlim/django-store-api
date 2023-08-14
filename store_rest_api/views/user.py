from django.http import JsonResponse
from store_rest_api.services.user import UserService, UserSerializer, CreateUserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

@api_view(['POST', 'GET'])
def user_view(request):
    if request.method == 'POST':
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                validate_password(data['password'], user=None, password_validators=None)
            except ValidationError as e:
                print(e)
                return JsonResponse({'errors': e.messages}, status=422)
            return JsonResponse(serializer.validated_data, status=201)
            # user = UserService.create(serializer.validated_data)
            # serializer = UserSerializer(user)
            # return JsonResponse(serializer.data)
        return JsonResponse({'errors': serializer.errors}, status=422)
    elif request.method == 'GET':
        user = UserService.find_by_id(request.user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
