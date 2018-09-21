from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

#возвращает страницу со списком list
def main(request):

    return render(request, 'mainapp/index.html')
    
def products(request):
​
    return render(request, 'mainapp/catalog.html')

def contact(request):
​
    return render(request, 'mainapp/contacts.html')


