# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

GENDER = [
    ('male','MALE'),('female','FEMALE'),('other','OTHER')
]
COMMON_STATUS = [
    ('active','ACTIVE'),('inactive','INACTIVE')
    
]
PAYMENT_STATUS = [
    ('pending','PENDING'),('paid','PAID'),('failed','FAILED'),('refunded','REFUNDED'),('unknown','UNKNOWN')
]
ORDER_STATUS = [
    ('pending','PENDING'),('processing','PROCESSING'),('shipped','SHIPPED'),('delivered','DELIVERED'),('canceled','CANCELED'),('unknown','UNKNOWN')
]
DISCOUNT_TYPE = [
    ('percentage discount','P_DISCOUNT'),('fixed cart discounts','FC_DISCOUNT'),('fixed product discounts','FP_DISCOUNT')
]

class Users(AbstractUser):
    
    phone_number = PhoneNumberField(null=False,default = '')
    date_of_birth = models.DateField(null=False, default = '1900-01-01')
    gender = models.CharField(choices=GENDER,max_length=20,null=False,default=GENDER[0])  # This field type is a guess.
    newsletter_subscription = models.CharField(max_length=255, null=False,default='')
    profile_picture_url = models.ImageField(upload_to='user_images/',null=True)
    account_status = models.TextField(null=False,choices=COMMON_STATUS,default =COMMON_STATUS[1])  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'users'

class Categories(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,default='')
    parent = models.ForeignKey('self', models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = 'categories'

class Brands(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False,default='')
    logo_url = models.ImageField(upload_to='logo_images/',null=True)

    class Meta:
        managed = True
        db_table = 'brands'

class Products(models.Model):
    product_name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    price = models.FloatField(null=False,default=0)
    quantity = models.IntegerField(default=0,null=False)
    sku = models.CharField(max_length=255, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, models.CASCADE, null=False)
    brand = models.ForeignKey(Brands, models.CASCADE, null=False)
    # user = models.ForeignKey(Users~, models.CASCADE, null=False)
    class Meta:
        managed = True
        db_table = 'products'


class Reviews(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    comment = models.TextField( null=False)
    review_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'reviews'



class ProductReviews(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    comment = models.TextField( null=False)
    review_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_reviews'


class BillingAddresses(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    address_1 = models.CharField(max_length=255, null=False)
    address_2 = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    postal_code = models.IntegerField( null=False)
    phone_number = PhoneNumberField(null = False,default = '')

    class Meta:
        managed = True
        db_table = 'billing_addresses'


class ShippingAddresses(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    address_1 = models.CharField(max_length=255, null=False)
    address_2 = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    postal_code = models.IntegerField( null=False)
    phone_number = PhoneNumberField(null = False,default = '')


    class Meta:
        managed = True
        db_table = 'shipping_addresses'


class Wishlists(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField( null=False,default='')

    class Meta:
        managed = True
        db_table = 'wishlists'



class Coupons(models.Model):
    code = models.CharField(max_length=255, null=False,unique=True)
    description = models.TextField( null=False)
    discount_type = models.CharField(choices=DISCOUNT_TYPE,null=False)
    discount_amount = models.IntegerField( null=False,default=0)
    minimum_purchase = models.IntegerField(null=False,default=1)
    expiration_date = models.DateTimeField()
    usage_limit = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=COMMON_STATUS,null=False,default=COMMON_STATUS[1])

    class Meta:
        managed = True
        db_table = 'coupons'

class ProductQuestions(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    question = models.TextField( null=False)
    question_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = Truez
        db_table = 'product_questions'

class ProductAnswers(models.Model):
    user = models.ForeignKey(Products, models.CASCADE, null=False)
    question = models.ForeignKey(ProductQuestions, models.CASCADE, null=False)
    answer = models.TextField( null=False)
    answers_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'product_answers'


class ProductImages(models.Model):
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    url = models.ImageField(upload_to='product_images')
    alt_text = models.CharField(max_length=255, null=False)

    class Meta:
        managed = True
        db_table = 'product_images'


class ProductOptions(models.Model):
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)

    class Meta:
        managed = True
        db_table = 'product_options'





class ProductVariants(models.Model):
    product = models.ForeignKey(Products, models.CASCADE, null=False)
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(default=0,null=False)
    quantity = models.IntegerField( null=False,default=1)
    sku = models.CharField(max_length=255, null=False)

    class Meta:
        managed = True
        db_table = 'product_variants'




class Optionvalues(models.Model):
    option = models.ForeignKey(ProductOptions, models.CASCADE, null=False)
    value = models.IntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'option_values'


class Orders(models.Model):
    user = models.ForeignKey(Users, models.CASCADE, null=False)
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    shipping_address = models.ForeignKey(ShippingAddresses, models.CASCADE, null=False)
    billing_address = models.ForeignKey(BillingAddresses, models.CASCADE, null=False)
    status = models.CharField(choices=ORDER_STATUS,default=ORDER_STATUS[5],null=False)
    coupon = models.ForeignKey(Coupons, models.CASCADE, null=False)

    class Meta:
        managed = True
        db_table = 'orders'


class Payments(models.Model):
    order = models.ForeignKey(Orders, models.CASCADE, null=False)
    payment_date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=255, null=False)
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    payment_status = models.CharField(choices=PAYMENT_STATUS,null=False,default=PAYMENT_STATUS[4])

    class Meta:
        managed = True
        db_table = 'payments'











