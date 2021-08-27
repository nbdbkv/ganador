from django.urls import path

from apps.shop.views import (
    MainPageView, ProductsByCollectionView,
    ProductDetailView, AboutUsListView, ContactListView,
)

urlpatterns = [
    path('', MainPageView.as_view()),
    path('clothes/<int:collection_pk>/', ProductsByCollectionView.as_view()),
    path(
        'clothes/<int:collection_pk>/products/<int:product_pk>/',
        ProductDetailView.as_view()
    ),
    path('about_us/', AboutUsListView.as_view()),
    path('contacts/', ContactListView.as_view()),
]
