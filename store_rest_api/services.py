from store_rest_api.models import Store


class StoreService:
    def find_by_id(self, store_id):
        return Store.objects.get(pk=store_id)
