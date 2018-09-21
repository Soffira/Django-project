from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

#возвращает страницу со списком list
def products_catalog(request):

    context = {
        'results' : [
            'Аквамарин',
            'Лазурит',
            'Змеевик',
        ]
    }
    return render(request, 'products/catalog.html', context)
    
def products_detail(request):

    return render(request, 'products/detail.html', {})
    
def products_create(request):

    return render(request, 'products/create.html', {})


