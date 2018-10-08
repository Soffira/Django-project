#urls для categories
from django.urls import path
from products.views.categories import (category_create)

app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='create'),
    # path('update/<int:pk>/', products.product_update, name='update'),
    # path('<int:pk>/', products.product_detail, name='detail'),
    # path('', products.product_catalog, name='catalog'),
]

'products:create'
'categories:create'
