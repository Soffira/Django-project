#urls для products
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', views.product_detail, name='detail'),
    path('get_template/', views.get_catalog_template),
    path('render_to_string/', views.render_catalog_to_string),
    path('native/', views.native),
    path('', views.product_catalog, name='catalog'),
]