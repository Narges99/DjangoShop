from django.shortcuts import render
from .forms import CategoryForm, ProductForm


def create_category(request):
    success_message = None
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Category created successfully!"
    else:
        form = CategoryForm()

    return render(request, 'products/create_category.html', {'form': form, 'success_message': success_message})


def create_product(request):
    success_message = None
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Product created successfully!"
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form, 'success_message': success_message})
