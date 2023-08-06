from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from store_rest_api import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("user/auth", views.UserAuthenticationView.as_view(), name="user_auth"),
    path("stores", views.StoreListView.as_view(), name="stores_list"),
    path("store/<int:store_id>", views.StoreView.as_view(), name="store"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]