from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_2gis_maps.admin import DoubleGisAdmin

from apps.shop.utils import ImageGet
from apps.shop.models import (
    Banner, Collection, Size, Detail, Image, Product, AboutUs, Contact, Rental,
)


@admin.register(Banner)
class BannerAdmin(ImageGet, admin.ModelAdmin):
    list_display = (
        'id', 'name', 'url_name', 'get_image', 'in_main', 'in_clothes',
        'in_about_us',
    )
    list_display_links = ('name', 'url_name',)
    list_editable = ('in_main', 'in_clothes', 'in_about_us',)


@admin.register(Collection)
class CollectionAdmin(ImageGet, admin.ModelAdmin):
    list_display = (
        'id', 'name', 'get_image', 'created_at', 'updated_at', 'is_active',
    )
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class ImageInline(ImageGet, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_image',)


class DetailAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Detail
        fields = ('title', 'description',)


class DetailInline(admin.StackedInline):
    form = DetailAdminForm
    model = Detail
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'collection', 'price', 'discount_price', 'created_at',
        'updated_at', 'is_active',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'collection__name',)
    list_filter = ('collection', 'size',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_editable = ('is_active',)
    inlines = [ImageInline, DetailInline]


class AboutUsAdminForm(forms.ModelForm):
    title = forms.CharField(
        label='Заголовок', widget=CKEditorUploadingWidget()
    )
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = AboutUs
        fields = ('title', 'description',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm
    list_display = ('id', 'title', 'description',)
    list_display_links = ('title', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'phone', 'whatsapp', 'mail', 'instagram', 'vk', 'work_time',
    )
    list_display_links = (
        'phone', 'whatsapp', 'mail', 'instagram', 'vk', 'work_time',
    )


@admin.register(Rental)
class RentalAdmin(DoubleGisAdmin):
    multiple_markers = False
    list_display = ('id', 'address', 'geolocation',)
    list_display_links = ('address', 'geolocation',)
