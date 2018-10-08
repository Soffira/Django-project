from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.shortcuts import get_object_or_404

#возвращает страницу со списком list
def main(request):
    # title = 'главная'
    # products = Product.objects.all()
    # content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', {})

def products(request, pk=None):
    print(pk)

    title = 'камни'
    links_menu = Category.objects.all()
     
    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }
        return render(request, 'products/products_list.html', content)
    same_products = Product.objects.all()[3:5]
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'products/products.html', content)

def contact(request):
    # title = 'о нас'
    # visit_date = datetime.datetime.now()
    # locations = [
        # {
            # 'city': 'Москва',
            # 'phone': '+7-495-000-0000',
            # 'email': 'info@geekshop.ru',
            # 'address': 'В пределах МКАД',
        # },
    # ]
    # content = {'title': title, 'visit_date':visit_date, 'locations': locations}
    return render(request, 'mainapp/contacts.html', {})
