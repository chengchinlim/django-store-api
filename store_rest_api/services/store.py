from store_rest_api.models.store import Store
from rest_framework import serializers

from store_rest_api.services.user import UserSerializer


class StoreService:
    @staticmethod
    def find_one(store_id, user_id):
        return Store.objects.get(id=store_id, user_id=user_id)

    @staticmethod
    def find_by_user_id(user_id):
        return Store.objects.filter(user_id=user_id)

    @staticmethod
    def find_all():
        return Store.objects.all()

    @staticmethod
    def create(name):
        Store.objects.create(name=name)


class StoreSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'created_at', 'updated_at', 'user')

