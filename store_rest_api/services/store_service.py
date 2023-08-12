from store_rest_api.models.store import Store
from rest_framework import serializers


class StoreService:
    @staticmethod
    def find_by_id(store_id):
        return Store.objects.get(pk=store_id)

    @staticmethod
    def find_all():
        return Store.objects.all()

    @staticmethod
    def create(name):
        Store.objects.create(name=name)


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

