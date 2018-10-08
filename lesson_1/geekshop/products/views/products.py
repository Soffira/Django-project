from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.views import View
from django.views.generic import (
    FormView, CreateView, UpdateView, 
    DeleteView, ListView, DetailView,
)
from django.urls import reverse_lazy
from django.http import HttpResponse
from products.models import Product
from products.forms import ProductModelForm

class ProductList(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'results'
    
#возвращает страницу со списком list
def product_catalog(request):

    query = get_list_or_404(Product)
    #query = models.Product.objects.all()

    return render(request, 'products/catalog.html', {'results': query})
    
class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'instance'
    
def product_detail(request, pk):

    obj = get_object_or_404(Product, id=pk)
    #obj = models.Product.objects.get(id=pk)

    return render(request, 'products/detail.html', {'instance': obj})
    
class ProductGenericCreate(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    
class ProductGenericUpdate(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    
class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:catalog')

class ProductCreate(View):
    success_url = reverse_lazy('products:catalog')
    def get(self, request):
        form = ProductModelForm()
        return render(request, 'products/create.html', {'form': form})
    def post(self, request):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, 'products/create.html', {'form': form})

def product_create(request):
    success_url = reverse_lazy('products:catalog')
    form = ProductModelForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(request, 'products/create.html', {'form': form})
    
class ProductUpdate(FormView):
    form_class = ProductModelForm
    success_url = reverse_lazy('products:catalog')
    template_name = 'products/create.html'
    def post(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        form = self.form_class(
            request.POST,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        return render(request, 'products/create.html', {'form': form})

    
def product_update(request, pk):
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Product, pk=pk)
    form = ProductModelForm(instance=obj)
    
    if request.method == 'POST':
        form = ProductModelForm(
            request.POST,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'products/create.html', {'form': form})

# def native(request):
    # template = Template('Hello {{ name }}')
    # context = Context({'name': 'Anton'})
    # response_string = template.render(context)
    # return HttpResponse(response_string)
    #Возможные варианты

# def get_catalog_template(request):
    # context = {
        # 'results' : ['Аквамарин', 'Лазурит', 'Змеевик',]
    # }
    # template = get_template('products/catalog.html')
    # # context = Context(context)
    # return HttpResponse(template.render(context))
    # #Возможные варианты
    
# def render_catalog_to_string(request):
    # context = {
        # 'results' : ['Аквамарин', 'Лазурит', 'Змеевик',]
    # }
    # return HttpResponse(render_to_string('products/catalog.html', context))
    # #Возможные варианты