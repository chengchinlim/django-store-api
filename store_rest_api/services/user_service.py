from django.contrib.auth.models import User
from rest_framework import serializers


class UserService:
    @staticmethod
    def find_by_id(user_id):
        return User.objects.get(pk=user_id)


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