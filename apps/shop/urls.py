from django.urls import path

from apps.shop.views import (
    IndexListView, ClothesListSerializer, ProductsByCollectionView,
    ProductDetailView, AboutUsListView, ContactListView,
)

urlpatterns = [
    path('', IndexListView.as_view()),
    path('clothes/', ClothesListSerializer.as_view()),
    path('clothes/<int:collection_pk>/', ProductsByCollectionView.as_view()),
    path(
        'clothes/<int:collection_pk>/products/<int:product_pk>/',
        ProductDetailView.as_view()
    ),
    path('about_us/', AboutUsListView.as_view()),
    path('contacts/', ContactListView.as_view()),
]
