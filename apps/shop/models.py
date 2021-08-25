from unidecode import unidecode

from django.db import models
from django.template import defaultfilters

from django_2gis_maps import fields as map_fields
from django_2gis_maps.mixins import DoubleGisMixin


def image_upload_to(instance, filename):
    if isinstance(instance, Banner):
        banner_name = defaultfilters.slugify(unidecode(instance.name))
        return f'banner/{banner_name}/{filename}'
    elif isinstance(instance, Collection):
        collection_name = defaultfilters.slugify(unidecode(instance.name))
        return f'collection/{collection_name}/{filename}'
    elif isinstance(instance, Image):
        collection_name = defaultfilters.slugify(
            unidecode(instance.product.collection.name)
        )
        product_name = defaultfilters.slugify(
            unidecode(instance.product.name)
        )
        return f'collection/{collection_name}/{product_name}/{filename}'


class Abstract(models.Model):
    """Abstract base class with common information for other models."""
    name = models.CharField(
        max_length=120, unique=True, verbose_name='Название',
    )
    slug = models.SlugField(max_length=120, unique=True,)
    is_active = models.BooleanField(verbose_name='Отобразить на странице',)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления',
    )

    class Meta:
        abstract = True


class Banner(models.Model):
    """Model for creating a Banner object."""
    name = models.CharField(
        max_length=120, blank=True, verbose_name='Название баннера',
    )
    url_name = models.CharField(
        max_length=60, blank=True, verbose_name='Название ccылки',
    )
    url = models.URLField(
        max_length=200, blank=True, verbose_name='Сcылка',
    )
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )
    in_main = models.BooleanField(verbose_name='Главная страница',)
    in_clothes = models.BooleanField(verbose_name='Одежда',)
    in_about_us = models.BooleanField(verbose_name='О нас',)

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name


class Collection(Abstract):
    """Model for creating a Collection object."""
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Size(models.Model):
    """Model for creating a Size object for Product."""
    name = models.CharField(
        max_length=15, unique=True, verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Product(Abstract):
    """Model for creating a Product object."""
    short_description = models.CharField(
        max_length=120, verbose_name='Краткое описание',
    )
    description = models.TextField(verbose_name='Описание',)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, verbose_name='Цена',
    )
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True,
        verbose_name='Цена со скидкой',
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


class Detail(models.Model):
    """Model for creating a Detail object for Product."""
    title = models.CharField(
        max_length=120, blank=True, verbose_name='Заголовок',
    )
    description = models.TextField(blank=True, verbose_name='Описание',)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='details',
        verbose_name='Товар',
    )

    class Meta:
        verbose_name = 'Детали продукта'
        verbose_name_plural = 'Детали продукта'

    def __str__(self):
        return self.product.name


class Image(models.Model):
    """Model for creating an Image object for Product."""
    image = models.ImageField(
        upload_to=image_upload_to, verbose_name='Изображение',
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images',
        verbose_name='Товар',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.product.name


class AboutUs(models.Model):
    """Model for creating a AboutUs object."""
    title = models.CharField(
        max_length=120, blank=True, verbose_name='Заголовок'
    )
    description = models.TextField(blank=True, verbose_name='Описание',)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Model for creating a Contact object."""
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
    phone = models.CharField(
        max_length=20, blank=True, verbose_name='Номер телефона'
    )
    work_time = models.CharField(
        max_length=60, blank=True, verbose_name='Рабочее время'
    )

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone


class Rental(DoubleGisMixin, models.Model):
    """Model for creating a Rental object."""
    address = map_fields.AddressField(max_length=200, verbose_name='Адрес')
    geolocation = map_fields.GeoLocationField(verbose_name='Геолокация')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.address
