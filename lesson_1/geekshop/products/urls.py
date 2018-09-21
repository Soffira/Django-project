#urls для products
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_catalog),
    path('detail/', views.products_detail),
    path('create/', views.products_create),
]