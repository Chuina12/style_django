from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seconde', views.seconde, name='seconde')
]