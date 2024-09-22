from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello_root'),  # Отвечает на корневой URL
    path('hello/', views.hello, name='hello'),  # Отвечает на /hello/
]