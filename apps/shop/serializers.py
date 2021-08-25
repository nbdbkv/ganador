from rest_framework import serializers

from .models import (
    Banner, Collection, Image, Product, Detail, AboutUs, Contact, Rental,
)


class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id', 'name', 'url_name', 'url', 'image',)


class IndexCollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'slug', 'name', 'image',)


class CollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'slug', 'name',)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class ProductsByCollectionSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'slug', 'name', 'short_description', 'price',
            'discount_price', 'first_image',
        )

    def get_first_image(self, obj):
        request = self.context.get('request')
        first_image_url = obj.images.first().image.url
        return request.build_absolute_uri(first_image_url)


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('id', 'title', 'description',)


class ProductDetailSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(
        slug_field='name', read_only=True, many=True
    )
    details = DetailSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'slug', 'name', 'description', 'price', 'discount_price',
            'size', 'details', 'images',
        )


class AboutUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'title', 'description',)


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'whatsapp', 'mail', 'instagram', 'vk', 'phone', 'work_time',
        )


class RentalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'address', 'geolocation',)
