from django.db import models

from django_2gis_maps import fields as map_fields
from django_2gis_maps.mixins import DoubleGisMixin
from solo.models import SingletonModel

from apps.shop.utils import image_upload_to


class MainPageBanner(SingletonModel):
    """Model for creating a MainPageBanner object."""
    name = models.CharField(max_length=120, verbose_name='Заголовок',)
    url = models.URLField(max_length=200, verbose_name='Сcылка',)
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Баннер главной страницы'
        verbose_name_plural = 'Баннер главной страницы'

    def __str__(self):
        return self.name


class MainPageImage(models.Model):
    """Model for creating a MainPageImage object."""
    name = models.CharField(max_length=120, verbose_name='Заголовок',)
    url = models.URLField(max_length=200, verbose_name='Сcылка',)
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )
    my_order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name='Порядок',
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение главной страницы'
        verbose_name_plural = 'Изображения главной страницы'

    def __str__(self):
        return self.name


class Collection(models.Model):
    """Model for creating a Collection object."""
    name = models.CharField(
        max_length=120, unique=True, verbose_name='Название',
    )
    slug = models.SlugField(max_length=120, unique=True,)
    in_slider = models.BooleanField(
        verbose_name='В слайдере главной страницы',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления',
    )
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )
    my_order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name='Порядок',
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Size(models.Model):
    """Model for creating a Size object for Product."""
    name = models.CharField(
        max_length=15, unique=True, verbose_name='Название',
    )
    my_order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name='Порядок',
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Model for creating a Product object."""
    name = models.CharField(
        max_length=120, unique=True, verbose_name='Название',
    )
    slug = models.SlugField(max_length=120, unique=True,)
    short_description = models.CharField(
        max_length=120, verbose_name='Краткое описание',
    )
    description = models.TextField(verbose_name='Описание',)
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, verbose_name='Цена',
    )
    new_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, verbose_name='Новая цена',
    )
    is_active = models.BooleanField(verbose_name='Отобразить на странице',)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления',
    )
    collection = models.ForeignKey(
        to=Collection, on_delete=models.CASCADE,
        related_name='collection_products', verbose_name='Коллекция',
    )
    size = models.ManyToManyField(
        to=Size, related_name='size_products', verbose_name='Размер',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class ProductAdditional(models.Model):
    """Model for creating a ProductAdditional object for Product."""
    title = models.CharField(
        max_length=120, blank=True, verbose_name='Заголовок',
    )
    description = models.TextField(blank=True, verbose_name='Описание',)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='additionals',
        verbose_name='Товар',
    )
    my_order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name='Порядок',
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Дополнительные характеристики товара'
        verbose_name_plural = 'Дополнительные характеристики товара'

    def __str__(self):
        return self.product.name


class ProductImage(models.Model):
    """Model for creating a ProductImage object for Product."""
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images',
        verbose_name='Товар',
    )
    my_order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name='Порядок',
    )

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.product.name


class AboutUs(SingletonModel):
    """Model for creating an AboutUs object."""
    description = models.TextField(blank=True, verbose_name='О Ganador',)
    title_production = models.CharField(
        max_length=120, verbose_name='Продукция Ganador'
    )
    text_production = models.TextField(blank=True, verbose_name='Описание',)
    title_manufacture = models.CharField(
        max_length=120, verbose_name='Одежда под ключ'
    )
    text_manufacture = models.TextField(blank=True, verbose_name='Описание',)
    fabric_image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение фабрики',
    )
    image_1 = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение 1',
    )
    url_1 = models.URLField(max_length=200, verbose_name='Сcылка 1',)
    image_2 = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение 2',
    )
    url_2 = models.URLField(max_length=200, verbose_name='Сcылка 2',)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.description


class Contact(DoubleGisMixin, SingletonModel):
    """Model for creating a Contact object."""
    address = map_fields.AddressField(max_length=200, verbose_name='Адрес')
    geolocation = map_fields.GeoLocationField(verbose_name='Геолокация')
    whatsapp = models.CharField(
        max_length=20, blank=True, verbose_name='WhatsApp'
    )
    mail = models.EmailField(
        max_length=60, blank=True, verbose_name='Электронная почта'
    )
    instagram = models.CharField(
        max_length=60, blank=True, verbose_name='Инстаграм'
    )
    vk = models.CharField(max_length=30, blank=True, verbose_name='ВКонтакте')
    phone_1 = models.CharField(
        max_length=20, blank=True, verbose_name='Номер телефона 1'
    )
    phone_2 = models.CharField(
        max_length=20, blank=True, verbose_name='Номер телефона 2'
    )
    work_time = models.CharField(
        max_length=60, blank=True, verbose_name='Рабочее время'
    )

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address
