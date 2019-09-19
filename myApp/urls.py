from django.urls import path
from . import views
from .views import MytestView

urlpatterns = [
    path('', views.index, name='index'),
    path('test/',  MytestView.as_view(), name='test'),
    path('getdata/',  views.getdata, name='getdata'),
]
