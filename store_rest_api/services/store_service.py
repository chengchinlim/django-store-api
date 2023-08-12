from store_rest_api.models.store import Store


class StoreService:
    @staticmethod
    def find_by_id(store_id):
        return Store.objects.get(pk=store_id)
