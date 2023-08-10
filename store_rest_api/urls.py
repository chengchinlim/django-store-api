from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from store_rest_api import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("user/auth", views.UserAuthenticationView.as_view(), name="user_auth"),
    path('jwt/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path("stores", views.StoreListView.as_view(), name="stores_list"),
    path("store", views.StoreView.as_view(), name="store"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]