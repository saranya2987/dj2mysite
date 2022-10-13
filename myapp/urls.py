from django.urls import path,include
from .views import index, new_one, my_place, products

urlpatterns = [
    path('',index),
    path('new',new_one),
    path('place',my_place),
    path('products',products),
]