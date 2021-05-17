from django import forms
from app.models import ProductModel

class ProductForm(forms.ModelForm):
    class meta:
        fields="__all__"
        model=ProductModel
