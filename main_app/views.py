from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# products logic
@login_required
def products_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'products/products_list.html', {'products': products})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                messages.success(request, "Product created successfully.")
                return redirect('products_list')
            except IntegrityError:
                messages.error(request, "A product with this code already exists. Please enter a unique code.")
                return render(request, 'create_product.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products_list')
    