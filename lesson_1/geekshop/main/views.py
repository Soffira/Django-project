from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse

#возвращает страницу со списком contact

def main_index(request):

    return render(request, 'main/index.html', {})