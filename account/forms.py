from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout,Row,Column
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from django.forms.widgets import SelectDateWidget
from ecommerce_app.models import Users,GENDER
from datetime import datetime as dt



class SignUpForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

class UpdateProfileForm(forms.Form):
    
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'disabled':True,'class': 'form-control'}),required=False)
    first_name = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email Address',widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = PhoneNumberField(widget=PhoneNumberInternationalFallbackWidget())
    gender = forms.ChoiceField(choices=GENDER)
    DoB = forms.DateField(label='Date of Birth',widget=SelectDateWidget(years=range(dt.now().year-100,dt.now().year+1)))
    subscription = forms.CharField(label='Newsletter Subscription',widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your phone number',
        })


