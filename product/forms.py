from django import forms
from ecommerce_app.models import Users,DISCOUNT_TYPE
from django.forms.widgets import SelectDateWidget
from datetime import datetime as dt

class CreateProductForm(forms.Form):
    product_name = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    price = forms.FloatField(
        label='Price',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    quantity = forms.ChoiceField(
        label='Quantity',
        choices=[(i,str(i)) for i in range(1,100001)],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    sku = forms.CharField(
        label='SKU',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    product_description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    brand_name = forms.CharField(
        label='Brand',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    category_name = forms.CharField(
        label='Category',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )

class UpdateProductForm(forms.Form):
    product_name = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    price = forms.FloatField(
        label='Price',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    quantity = forms.ChoiceField(
        label='Quantity',
        choices=[(i,str(i)) for i in range(1,100001)],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    sku = forms.CharField(
        label='SKU',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    product_description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    brand_name = forms.CharField(
        label='Brand',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    category_name = forms.CharField(
        label='Category',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    
class CreateCouponForm(forms.Form):
    code = forms.CharField(
        label='Coupon Code',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    discount_type = forms.CharField(
        label='Discount Type',
        widget=forms.ChoiceField(choices=DISCOUNT_TYPE,attrs={'class': 'form-control'}),
        required=True,
    )
    discount_amount = forms.CharField(
        label='Discount Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    minimum_purchase = forms.CharField(
        label='Discount Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    expiration_date = forms.DateField(label='Date of Birth',widget=SelectDateWidget(years=range(dt.now().year)))

    usage_limit =  forms.CharField(
        label='Discount Amount',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    

    