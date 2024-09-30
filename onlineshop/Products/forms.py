from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent_category']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['upc', 'name', 'description', 'price', 'stock', 'category']
