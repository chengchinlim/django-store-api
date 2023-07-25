from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from store_rest_api import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("stores/", views.StoreListView.as_view(), name="store_list"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
]