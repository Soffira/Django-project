#urls для main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_index),
]