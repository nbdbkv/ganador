from django.utils.html import mark_safe


class ImageGet:
    @staticmethod
    def get_image(obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'
