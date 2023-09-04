from store_rest_api.models.product import Product
from store_rest_api.services.store import StoreService


class ProductService:
    @staticmethod
    def create(products, user_id):
        store = StoreService.find_by_user_id(user_id).first()
        for p in products:
            product = Product(name=p['name'], category=p['category'])
            product.save()
            store.products.add(product)
        store.save()
        return store.products
