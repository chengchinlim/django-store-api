from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from store_rest_api.services.user import UserService, UserSerializer, CreateUserSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer

    @extend_schema(responses={200: UserSerializer})
    def get(self, request):
        user = UserService.find_by_id(request.user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    @extend_schema(responses={200: UserSerializer})
    def create(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                validate_password(data['password'], user=None, password_validators=None)
            except ValidationError as e:
                print(e)
                return JsonResponse({'errors': e.messages}, status=422)
            # return JsonResponse(serializer.validated_data, status=201)
            user = UserService.create(data)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        return JsonResponse({'errors': serializer.errors}, status=422)
