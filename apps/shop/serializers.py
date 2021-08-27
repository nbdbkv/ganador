from rest_framework import serializers

from .models import (
    MainPageBanner, MainPageImage, Collection, ProductImage, Product,
    ProductAdditional, AboutUs, Contact,
)


class MainPageBannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageBanner
        fields = ('id', 'name', 'url', 'image',)


class MainPageImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageImage
        fields = ('id', 'name', 'url', 'image',)


class MainPageCollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'slug', 'name', 'image',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductsByCollectionSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'slug', 'name', 'short_description', 'old_price',
            'new_price', 'first_image',
        )

    def get_first_image(self, obj):
        request = self.context.get('request')
        first_image_url = obj.images.first().image.url
        return request.build_absolute_uri(first_image_url)


class ProductAdditionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAdditional
        fields = ('id', 'title', 'description',)


class ProductDetailSerializer(serializers.ModelSerializer):
    size = serializers.SlugRelatedField(
        slug_field='name', read_only=True, many=True
    )
    additionals = ProductAdditionalSerializer(many=True)
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id', 'slug', 'name', 'description', 'old_price', 'new_price',
            'size', 'additionals', 'images',
        )


class AboutUsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'id', 'description', 'title_production', 'text_production',
            'title_manufacture', 'text_manufacture', 'fabric_image', 'image_1',
            'url_1', 'image_2', 'url_2',
        )


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'address', 'geolocation', 'whatsapp', 'whatsapp', 'mail',
            'instagram', 'vk', 'phone_1', 'phone_2', 'work_time',
        )
