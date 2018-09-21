from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

#возвращает страницу со списком contact

def contact_contacts(request):

    return render(request, 'contact/contacts.html', {})