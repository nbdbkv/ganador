from unidecode import unidecode

from django.utils.html import mark_safe
from django.template import defaultfilters


def image_upload_to(instance, filename):
    class_name = defaultfilters.slugify(unidecode(instance.__class__.__name__))
    if hasattr(instance, 'name'):
        return (
            f'{class_name}/'
            f'{defaultfilters.slugify(unidecode(instance.name))}/{filename}'
        )
    elif hasattr(instance, 'product'):
        return (
            f'{class_name}/'
            f'{defaultfilters.slugify(unidecode(instance.product.name))}/'
            f'{filename}'
        )
    elif hasattr(instance, 'title_production'):
        return f'{class_name}/{filename}'


class ImageShow:
    @staticmethod
    def show_image(obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')
