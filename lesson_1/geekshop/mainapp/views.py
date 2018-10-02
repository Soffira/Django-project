from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from datetime import datetime

#возвращает страницу со списком list
def main(request):
    # title = 'главная'
    # products = Product.objects.all()
    # content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', {})

def products(request):
    # title = 'камни'
    # links_menu = ProductCategory.objects.all()
    # same_products = Product.objects.all()
    
    # content = {'title': title, 'links_menu': links_menu, 'same_products': same_products}
    return render(request, 'mainapp/catalog.html', {})

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
