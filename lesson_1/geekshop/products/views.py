from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from . import models

#возвращает страницу со списком list
def product_catalog(request):

    query = get_list_or_404(models.Product)
    #query = models.Product.objects.all()

    return render(request, 'products/catalog.html', {'results': query})
    
def product_detail(request, pk):

    obj = get_object_or_404(models.Product, id=pk)
    #obj = models.Product.objects.get(id=pk)

    return render(request, 'products/detail.html', {'instance': obj})
    
def product_create(request):
    return render(request, 'products/create.html', {})
    
def native(request):

    template = Template('Hello {{ name }}')

    context = Context({'name': 'Anton'})

    response_string = template.render(context)

    return HttpResponse(response_string)
    #Возможные варианты

def get_catalog_template(request):

    context = {
        'results' : [
            'Аквамарин',
            'Лазурит',
            'Змеевик',
        ]
    }
    template = get_template('products/catalog.html')
    # context = Context(context)
    return HttpResponse(template.render(context))
    #Возможные варианты
    
def render_catalog_to_string(request):

    context = {
        'results' : [
            'Аквамарин',
            'Лазурит',
            'Змеевик',
        ]
    }
    return HttpResponse(render_to_string('products/catalog.html', context))
    #Возможные варианты