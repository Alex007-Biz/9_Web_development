from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('goods', views.goods, name='goods'),
    path('services', views.service, name='services'),
]