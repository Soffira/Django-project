#urls для products
from django.urls import path
from products.views.products import (
    ProductCreate, ProductUpdate, ProductGenericCreate, 
    ProductGenericUpdate, ProductList, ProductDetail, ProductDelete,
    product_create, product_update, product_detail, product_catalog)

app_name = 'products'

urlpatterns = [
#    path('get_template/', products.get_catalog_template),
#    path('render_to_string/', products.render_catalog_to_string),
#    path('native/', products.native),
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='catalog'),
]