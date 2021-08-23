from django.db import models

from django_2gis_maps import fields as map_fields
from django_2gis_maps.mixins import DoubleGisMixin


class CommonInfo(models.Model):
    """Abstract base class with common information for other models."""
    name = models.CharField(
        max_length=120, unique=True, verbose_name='Название'
    )
    slug = models.SlugField(max_length=120, unique=True)
    is_active = models.BooleanField(verbose_name='Отобразить на странице')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата обновления'
    )

    class Meta:
        abstract = True


class Collection(CommonInfo):
    """Model for creating a Collection object."""
    image = models.ImageField(
        upload_to='Collections/', verbose_name='Изображение'
    )

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Product(CommonInfo):
    """Model for creating a Product object."""
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена со скидкой'
    )
    material = models.CharField(max_length=120, verbose_name='Материал')
    composition = models.CharField(max_length=120, verbose_name='Состав')
    season = models.CharField(max_length=30, verbose_name='Сезон')
    instruction = models.CharField(
        max_length=120, verbose_name='Инструкция по уходу'
    )
    collection = models.ForeignKey(
        to=Collection, on_delete=models.CASCADE,
        related_name='collection_products', verbose_name='Коллекция'
    )
    size = models.ManyToManyField(
        to='Size', related_name='size_products', verbose_name='Размер',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Size(models.Model):
    """Model for creating a Size object for Product."""
    name = models.CharField(
        max_length=15, unique=True, verbose_name='Название'
    )

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Image(models.Model):
    """Model for creating an Image object for Product."""
    image = models.ImageField(
        upload_to='Products/', verbose_name='Изображение'
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images',
        verbose_name='Товар'
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    """Model for creating a Delivery object."""
    delivery = models.TextField(blank=True, verbose_name='Доставка')
    term = models.TextField(blank=True, verbose_name='Условия')

    class Meta:
        verbose_name = 'Доставка и возврат'
        verbose_name_plural = 'Доставка и возврат'

    def __str__(self):
        return f'{self.delivery}, {self.term}'


class AboutUs(models.Model):
    """Model for creating a AboutUs object."""
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.description


class Contact(models.Model):
    """Model for creating a Contact object."""
    address = models.CharField(
        max_length=120, blank=True, verbose_name='Адрес'
    )
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
        return self.address


class Rental(DoubleGisMixin, models.Model):
    """Model for creating a Rental object."""
    address = map_fields.AddressField(max_length=200, verbose_name='Адрес')
    geolocation = map_fields.GeoLocationField(verbose_name='Геолокация')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.address
