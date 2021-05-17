from django.shortcuts import render
from app.models import ProductModel
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from django.views.generic import UpdateView

# Create your views here.
class AddProduct(CreateView):
    template_name = 'add_product.html'
    model = ProductModel
    success_url = '/view_all_products/'
    fields = "__all__"


class ViewAllProduct(ListView):
    template_name = 'view_all_product.html'
    model = ProductModel
    success_url= '/index/'
    fields="__all__"


class DeleteProduct(DeleteView):
    template_name = 'delete_product.html'
    model = ProductModel
    fields="__all__"
    success_url='/view_all_products/'

class UpdateProduct(UpdateView):
     template_name = "Update_Product.html"
     model = ProductModel
     fields = "__all__"
     success_url = '/view_all_products/'
