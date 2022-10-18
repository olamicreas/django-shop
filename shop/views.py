from atexit import register
import builtins
import collections
from copyreg import pickle
from distutils.command.install_egg_info import safe_name
from email.mime import image
from heapq import merge
import json
from unicodedata import name
from django.views.generic.list import ListView
from itertools import chain, product
from math import prod
from multiprocessing import context
from django.contrib import messages
from typing import ChainMap, Mapping
from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse
from django.core import serializers
from django import template
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from haystack.query import SearchQuerySet

from pypaystack import Transaction, Customer, Plan



register = template.Library()
# Create your views here.

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False



def store(request):
    product = Product.objects.all()
    

    context = {
        'product': product,
        
    }

    return render(request, 'shop/store.html', context)

class ProductView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/store.html'
    ordering = ['name']
    paginate_by = 5



def cart(request):
    if not request.user.is_authenticated:
        messages.warning(request, f'Login first')
        return redirect('login')
    carting = request.session['cart']
    keys = list(request.session['cart'].keys())
    for k in keys:
        k
    cartss = Product.objects.get(id=k)
    col = cartss.colors.split(',')

    subtotal = 0
    grandtotal = 0
    for key, product in carting.items():

        discount = (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        
        deliveryFee = ("%.2f" % (.004 * float(subtotal)))
        grandtotal = float("%.2f" % (1.06 * subtotal))
        email = request.user.email

       
   
    context = {'cart': carting ,'product': product,'discount': discount, 'subtotal': subtotal , 'deliveryFee': deliveryFee, 'grandtotal': grandtotal, 'cartss': col, email :'email'}
   
    
    return render(request, 'shop/cart.html', context)

def single(request, pk):
    product = Product.objects.get(id=pk)
    col = product.colors.split(',')
    context = {
        'product': product,
        'col': col
    }
    return render (request, 'shop/single.html', context)


def addcart(request):
    
   
    
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')
    colors = request.POST.get('colors')
    
    product = Product.objects.get(id=product_id)
    

    
    DictItems = {product_id:{'name': product.name, 'price': product.price, 'discount': product.discount, 'stock': product.stock, 'quantity': quantity, 'color': colors, 'image': product.image1.url, 'colors': product.colors }
    }
    json.dumps(DictItems)
        
    if 'cart' in request.session:
        if product_id in request.session['cart']:
            print("Product alreaady in your cart")
        
        else:

            request.session['cart'] = MagerDicts(request.session['cart'], DictItems)
        
        if len(request.session['cart']) > 5:
            request.session['cart'].pop()


        
    else:
        request.session['cart'] = DictItems
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    request.session.modified = True

      

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
   

def checkout(request):
    request.session.pop('cart', None)

    return render(request, 'shop/checkout.html')

class SearchView(ListView):
    model = Product
    template_name = 'shop/store.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('pname')
        context['product'] = Product.objects.filter(name__icontains=name)
        
        return context



def searching(request):
    result = SearchQuerySet().filter(content=request.GET.get('pname'))
    
    return render(request, 'search/search.html', {'result': result})