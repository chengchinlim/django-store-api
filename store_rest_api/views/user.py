from django.http import JsonResponse
from rest_framework.generics import RetrieveUpdateAPIView
from store_rest_api.services.user_service import UserService, UserSerializer


class UserView(RetrieveUpdateAPIView):
    def get(self, request, **kwargs):
        user = UserService.find_by_id(request.user_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)