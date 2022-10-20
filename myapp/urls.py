from django.urls import path,include
from .views import index, new_one, my_place, products, product_details, add_product
urlpatterns = [
    path('',index),
    path('new/',new_one),
    path('place',my_place),
    path('products/',products, name='products'),
    path('products/<int:id>',product_details,name='product_details'),
    path('products/add',add_product,name='add_product'),
    path('__reload__/', include('django_browser_reload.urls')),

]