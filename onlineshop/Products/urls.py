from django.urls import path
from Products.views import *


urlpatterns = [
    path('create-category/', create_category, name='create_category'),
    path('create-product/', create_product, name='create_product'),

]