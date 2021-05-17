"""crudwithcbvbynaveen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from app.models import EmployeeModel




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',TemplateView.as_view(template_name='index.html'),name='main'),
    path('add_product/',views.AddProduct.as_view(),name='add_product'),
    path('view_all_products/',views.ViewAllProduct.as_view(),name='view_all_products'),
    path('delete_product/<int:pk>',views.DeleteProduct.as_view(),name='delete_product'),
    path('update_product/<int:pk>', views.UpdateProduct.as_view(), name='update_product'),

    ###<int:pk> primary key with interger tag
    ##createview example,listview example without views.py
    path('add_employee/',CreateView.as_view(template_name='add_employee.html',fields="__all__",model=EmployeeModel,success_url='/view_all_employee/'),name='add_employee'),
    path('view_all_employee/',ListView.as_view(template_name='view_all_employee.html',model=EmployeeModel),name='view_all_employee'),
    path('view_all_employee/', ListView.as_view(template_name='view_all_employee.html', model=EmployeeModel),  name='view_all_employee'),

]
