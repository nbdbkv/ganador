from django.contrib import admin
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_2gis_maps.admin import DoubleGisAdmin

from apps.shop.models import (
    Collection, Size, Product, Image, AboutUs, Contact, Rental, Delivery
)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'is_active',)
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'collection', 'price', 'discount_price', 'created_at',
        'updated_at',  'is_active',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'collection__name',)
    list_filter = ('collection', 'size',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_editable = ('is_active',)
    inlines = [ImageInline]


class DeliveryAdminForm(forms.ModelForm):
    delivery = forms.CharField(
        label='Доставка и возврат', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Delivery
        fields = ('delivery', 'term',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display = ('id', 'delivery', 'term',)
    list_display_links = ('delivery', 'term',)


class AboutUsAdminForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание', widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = AboutUs
        fields = ('description',)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm
    list_display = ('id', 'description',)
    list_display_links = ('description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'address', 'whatsapp', 'mail', 'instagram', 'vk', 'phone',
        'work_time',
    )
    list_display_links = (
        'address', 'whatsapp', 'mail', 'instagram', 'vk', 'phone', 'work_time',
    )


@admin.register(Rental)
class RentalAdmin(DoubleGisAdmin):
    multiple_markers = False
    list_display = ('id', 'address', 'geolocation',)
    list_display_links = ('address', 'geolocation',)
