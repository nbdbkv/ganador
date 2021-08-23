from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class ExampleView(TemplateView):
    template_name = 'example.html'
