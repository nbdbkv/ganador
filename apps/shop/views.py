from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.shop.models import (
    Collection, Product, Delivery, AboutUs, Contact, Rental
    )
from apps.shop.serializers import (
    IndexCollectionListSerializer, CollectionListSerializer,
    ProductsByCollectionSerializer, ProductDetailSerializer,
    DeliveryListSerializer, AboutUsListSerializer, ContactListSerializer,
    RentalListSerializer,
)


class IndexCollectionListView(ListAPIView):
    queryset = Collection.objects.filter(is_active=True)
    serializer_class = IndexCollectionListSerializer


class CollectionListView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer


class ProductsByCollectionView(ListAPIView):
    serializer_class = ProductsByCollectionSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'collection_pk'

    def get_queryset(self):
        return Product.objects.filter(
            is_active=True,
            collection_id=self.kwargs['collection_pk']
        ).prefetch_related('images')


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_pk'


class DeliveryListView(ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliveryListSerializer


class AboutUsListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializer


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer


class RentalListView(ListAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalListSerializer
