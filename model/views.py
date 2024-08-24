from django.shortcuts import render
from  .models import Category, Product, Customer


def category(request):
    categories = Category.objects.all()
    context = {
        'title':  'Categoriyalar',
        'categories': categories,
    }
    return render(request, 'category.html', context)


def product(request):
    products = Product.objects.all()
    context = {
        'title': 'Mahsulotlar',
        'products': products,
    }
    return render(request, 'product.html', context)


def customer(request):
    customers = Customer.objects.all()
    context = {
        'title': 'Xaridorlar',
        'customers': customers,
    }
    return render(request, 'customer.html', context)

