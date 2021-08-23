# Generated by Django 3.2.6 on 2021-08-22 12:10

from django.db import migrations, models
import django.db.models.deletion
import django_2gis_maps.fields
import django_2gis_maps.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('is_active', models.BooleanField(verbose_name='Отобразить на странице')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('image', models.ImageField(upload_to='Collections/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=120, verbose_name='Адрес')),
                ('whatsapp', models.CharField(blank=True, max_length=20, verbose_name='WhatsApp')),
                ('mail', models.EmailField(blank=True, max_length=60, verbose_name='Электронная почта')),
                ('instagram', models.CharField(blank=True, max_length=60, verbose_name='Инстаграм')),
                ('vk', models.CharField(blank=True, max_length=30, verbose_name='ВКонтакте')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('work_time', models.CharField(blank=True, max_length=60, verbose_name='Рабочее время')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.TextField(blank=True, verbose_name='Доставка')),
                ('term', models.TextField(blank=True, verbose_name='Условия')),
            ],
            options={
                'verbose_name': 'Доставка и возврат',
                'verbose_name_plural': 'Доставка и возврат',
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_2gis_maps.fields.AddressField(max_length=200, verbose_name='Адрес')),
                ('geolocation', django_2gis_maps.fields.GeoLocationField(verbose_name='Геолокация')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
            bases=(django_2gis_maps.mixins.DoubleGisMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('is_active', models.BooleanField(verbose_name='Отобразить на странице')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата обновления')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена со скидкой')),
                ('material', models.CharField(max_length=120, verbose_name='Материал')),
                ('composition', models.CharField(max_length=120, verbose_name='Состав')),
                ('season', models.CharField(max_length=30, verbose_name='Сезон')),
                ('instruction', models.CharField(max_length=120, verbose_name='Инструкция по уходу')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_products', to='shop.collection', verbose_name='Коллекция')),
                ('size', models.ManyToManyField(related_name='size_products', to='shop.Size', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Products/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]