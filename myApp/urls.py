from django.urls import path
from . import views
from .views import BaseView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('base/',  BaseView.as_view(), name='base'),
    path('getdata/',  views.getdata, name='getdata'),
]
