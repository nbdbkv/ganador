from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_2gis_maps.admin import DoubleGisAdmin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from apps.shop.utils import ImageShow
from apps.shop.models import (
    MainPageBanner, MainPageImage, Collection, Size, ProductAdditional,
    ProductImage, Product, AboutUs, Contact,
)


@admin.register(MainPageBanner)
class MainPageBannerAdmin(ImageShow, admin.ModelAdmin):
    list_display = ('name', 'url', 'show_image',)
    list_display_links = ('name',)
    ImageShow.show_image.short_description = 'Изображение'


@admin.register(MainPageImage)
class MainPageImageAdmin(SortableAdminMixin, ImageShow, admin.ModelAdmin):
    list_display = ('name', 'url', 'show_image', 'my_order',)
    list_display_links = ('name',)
    ImageShow.show_image.short_description = 'Изображение'


@admin.register(Collection)
class CollectionAdmin(SortableAdminMixin, ImageShow, admin.ModelAdmin):
    list_display = (
        'name', 'created_at', 'updated_at', 'show_image', 'in_slider',
        'my_order',
    )
    list_display_links = ('name',)
    ImageShow.show_image.short_description = 'Изображение'
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('in_slider',)


@admin.register(Size)
class SizeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'my_order',)
    list_display_links = ('name',)


class ProductImageInline(
    SortableInlineAdminMixin, ImageShow, admin.TabularInline
):
    model = ProductImage
    extra = 1
    readonly_fields = ('show_image',)
    ImageShow.show_image.short_description = 'Изображение'


class ProductAdditionalAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = ProductAdditional
        fields = ('description',)


class ProductAdditionalInline(SortableInlineAdminMixin, admin.StackedInline):
    form = ProductAdditionalAdminForm
    model = ProductAdditional
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'collection', 'old_price', 'new_price', 'created_at',
        'updated_at', 'is_active',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'collection__name',)
    list_filter = ('collection', 'size',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_editable = ('is_active',)
    inlines = (ProductImageInline, ProductAdditionalInline)


class AboutUsAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = AboutUs
        fields = (
            'id', 'description', 'title_production', 'text_production',
            'title_manufacture', 'text_manufacture', 'fabric_image', 'image_1',
            'url_1', 'image_2', 'url_2',
        )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm
    list_display = ('description',)
    list_display_links = ('description',)


@admin.register(Contact)
class ContactAdmin(DoubleGisAdmin):
    multiple_markers = False
    list_display = (
        'address', 'geolocation', 'whatsapp', 'mail', 'instagram', 'vk',
        'phone_1', 'phone_2', 'work_time',
    )
    list_display_links = ('address',)
