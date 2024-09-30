from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart, CartLine
from .forms import AddToCartForm


def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            if product.stock < quantity:
                return JsonResponse({'error': 'Product is out of stock'}, status=400)

            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_line, created = CartLine.objects.get_or_create(cart=cart, product=product)
            cart_line.quantity += quantity
            cart_line.save()

            product.stock -= quantity
            product.save()

            return JsonResponse({'message': f'{quantity} {product.name}{"s" if quantity > 1 else ""} added to cart successfully!'})
        else:
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = AddToCartForm()
        return render(request, 'carts/add_to_cart.html', {'form': form})

