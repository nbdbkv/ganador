from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.shop.models import (
    MainPageBanner, MainPageImage, Collection, Product, AboutUs, Contact
)
from apps.shop.serializers import (
    MainPageBannerListSerializer, MainPageImageListSerializer,
    MainPageCollectionListSerializer, ProductsByCollectionSerializer,
    ProductDetailSerializer, AboutUsListSerializer, ContactListSerializer,
)


class MainPageView(ListAPIView):
    queryset_banner = MainPageBanner.objects.all()
    queryset_collection = Collection.objects.filter(in_slider=True)
    queryset_image = MainPageImage.objects.all()
    serializer_class_banner = MainPageBannerListSerializer
    serializer_class_collection = MainPageCollectionListSerializer
    serializer_class_image = MainPageImageListSerializer

    def list(self, request, *args, **kwargs):
        banner = self.serializer_class_banner(
            self.queryset_banner, many=True, context={'request': request}
        )
        collection = self.serializer_class_collection(
            self.queryset_collection, many=True, context={'request': request}
        )
        image = self.serializer_class_image(
            self.queryset_image, many=True, context={'request': request}
        )

        return Response(
            {
                'banner': banner.data,
                'collection': collection.data,
                'image': image.data,
            }
        )


class ProductsByCollectionView(ListAPIView):
    serializer_class = ProductsByCollectionSerializer
    lookup_url_kwarg = 'collection_pk'

    def get_queryset(self):
        return Product.objects.filter(
            is_active=True,
            collection_id=self.kwargs['collection_pk']
        ).prefetch_related('images')


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_pk'

    def get_queryset(self):
        return Product.objects.filter(
            is_active=True,
            collection_id=self.kwargs['collection_pk']
        )


class AboutUsListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsListSerializer


class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactListSerializer
