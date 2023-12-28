# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy 

from django.template import loader
from .models import Product
from .forms import ProductForm
# from .models import Productlist


class ProductList(ListView): 
    model = Product
def testing(request):
    template = loader.get_template('base.html')
    context = {
        'firstname': 'Boss',
    }
    return HttpResponse(template.render(context, request))


class ProductDetail(DetailView): 
    model = Product
    # 

class ProductCreate(SuccessMessageMixin, CreateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    # produk = Product.object.get(id=id)
    # template = loader.get_template("product_detail.html")
    # context = {
    #     "produk": produk,
    # }
    success_message = "Product successfully created!"

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully updated!"

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product successfully deleted!"



