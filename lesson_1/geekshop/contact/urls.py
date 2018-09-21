#urls для main
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_contacts),
]