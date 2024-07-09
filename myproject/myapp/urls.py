from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('contact/', views.contact, name='contact'),
]
