from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views
from store_rest_api.views.home import HomeView
from store_rest_api.views.product_list import ProductListView
from store_rest_api.views.store import StoreView
from store_rest_api.views.store_list import StoreListView
from store_rest_api.views.user import UserView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('jwt/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("user", UserView.as_view(), name="user"),
    path("stores", StoreListView.as_view(), name="stores_list"),
    path("store", StoreView.as_view(), name="store"),
    path("products", ProductListView.as_view(), name="product_list"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]