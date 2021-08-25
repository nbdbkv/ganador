from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.shop.models import (
    Banner, Collection, Product, AboutUs, Contact, Rental
    )
from apps.shop.serializers import (
    BannerListSerializer, IndexCollectionListSerializer,
    CollectionListSerializer, ProductsByCollectionSerializer,
    ProductDetailSerializer, AboutUsListSerializer, ContactListSerializer,
    RentalListSerializer,
)


class IndexListView(ListAPIView):
    queryset_banner = Banner.objects.filter(in_main=True)
    queryset_collection = Collection.objects.filter(is_active=True)
    serializer_class_banner = BannerListSerializer
    serializer_class_collection = IndexCollectionListSerializer

    def list(self, request, *args, **kwargs):
        banner = self.serializer_class_banner(
            self.queryset_banner, many=True, context={'request': request}
        )
        collection = self.serializer_class_collection(
            self.queryset_collection, many=True, context={'request': request}
        )
        return Response({'banner': banner.data, 'collection': collection.data})


class ClothesListSerializer(ListAPIView):
    queryset_banner = Banner.objects.filter(in_clothes=True)
    queryset_collection = Collection.objects.all()
    serializer_class_banner = BannerListSerializer
    serializer_class_collection = CollectionListSerializer

    def list(self, request, *args, **kwargs):
        banner = self.serializer_class_banner(
            self.queryset_banner, many=True, context={'request': request}
        )
        collection = self.serializer_class_collection(
            self.queryset_collection, many=True
        )
        return Response({'banner': banner.data, 'collection': collection.data})


class ProductsByCollectionView(ListAPIView):
    serializer_class = ProductsByCollectionSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'collection_pk'

    def get_queryset(self):
        return Product.objects.filter(
            is_active=True,
            collection_id=self.kwargs['collection_pk']
        )


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_pk'


class AboutUsListView(ListAPIView):
    queryset_about_us = AboutUs.objects.all()
    queryset_banner = Banner.objects.filter(in_about_us=True)
    serializer_class_about_us = AboutUsListSerializer
    serializer_class_banner = BannerListSerializer

    def list(self, request, *args, **kwargs):
        about_us = self.serializer_class_about_us(
            self.queryset_about_us, many=True
        )
        banner = self.serializer_class_banner(
            self.queryset_banner, many=True, context={'request': request}
        )
        return Response({'about_us': about_us.data, 'banner': banner.data})


class ContactListView(ListAPIView):
    queryset_contacts = Contact.objects.all()
    queryset_rental = Rental.objects.all()
    serializer_class_contact = ContactListSerializer
    serializer_class_rental = RentalListSerializer

    def list(self, request, *args, **kwargs):
        contacts = self.serializer_class_contact(
            self.queryset_contacts, many=True
        )
        rental = self.serializer_class_rental(
            self.queryset_rental, many=True
        )
        return Response({'contacts': contacts.data, 'rental': rental.data})
