from django.urls import path

from apps.shop.views import (
    IndexCollectionListView, CollectionListView, ProductsByCollectionView,
    ProductDetailView, DeliveryListView, AboutUsListView, ContactListView,
    RentalListView,
)


urlpatterns = [
    path('', IndexCollectionListView.as_view()),
    path('clothes/', CollectionListView.as_view()),
    path('clothes/<int:collection_pk>/', ProductsByCollectionView.as_view()),
    path('clothes/<int:collection_pk>/products/<int:product_pk>/', ProductDetailView.as_view()),
    path('delivery/', DeliveryListView.as_view()),
    path('about_us/', AboutUsListView.as_view()),
    path('contacts/', ContactListView.as_view()),
    path('rental/', RentalListView.as_view()),
]
