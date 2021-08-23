from django.urls import path

from apps.templates_app.views import IndexView, ExampleView

urlpatterns = [
    path('example/', ExampleView.as_view(), name='example_page'),
    path('', IndexView.as_view(), name='index_page'),
]
