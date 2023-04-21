from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_product,name='createProduct'),
    path('create-coupon/',views.create_coupon,name='createCoupon')
]