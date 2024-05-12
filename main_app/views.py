from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

from django.contrib import messages
from .models import Product
from .forms import ProductForm

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if Product.objects.filter(code=code).exists():
                messages.error(request, f"A product with code '{code}' already exists.")
                return redirect('create_product')
            else:
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                messages.success(request, "Product created successfully.")
                return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})

    
# authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')