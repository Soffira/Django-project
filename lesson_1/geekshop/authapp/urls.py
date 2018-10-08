from django.urls import path
import authapp.views as authapp
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]