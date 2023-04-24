from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from ecommerce_app.models import Users,Categories,Brands,Products,Orders,Coupons,COMMON_STATUS
from .forms import CreateProductForm,UpdateProductForm,CreateCouponForm
from django.contrib import messages
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
# from django.core import serializers


#CRUD product(s)
@login_required
@user_passes_test(lambda user:user.is_staff)
# @require_GET
def create_product(request):
    # user_id  = request.user.id
    form = CreateProductForm()
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data['brand_name']
            brand = Brands.objects.filter(name = brand_name).first()
            category_name = form.cleaned_data['category_name']
            category = Categories.objects.filter(name = category_name).first()
            if not brand:
                messages.error(request,'Brand does not exist')
            elif not category:
                messages.error(request,'Category does not exist')
            else:
                product = Products.objects.create(product_name = form.cleaned_data['product_name'],
                                                  description = form.cleaned_data['product_description'],
                                                  price = form.cleaned_data['price'],
                                                  quantity = form.cleaned_data['quantity'],
                                                  sku = form.cleaned_data['sku'],
                                                  category = category,
                                                  brand = brand
                                                  )
                messages.success(request,'Successfully create new product')
            return redirect('createProduct')
    return render(request,'product/create-product.html',{'form':form})

@login_required
@user_passes_test(lambda user:user.is_staff)
def update_product(request,id):
    product = Products.objects.filter(pk=id).first()
    form = UpdateProductForm(initial={'product_name':product.product_name,
                                      'price': product.price,
                                      'quantity':product.quantity,
                                      'sku':product.sku,
                                      'product_description':product.description,
                                      'brand_name':product.brand.name,
                                      'category_name':product.category.name})
    if request.method =='POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            product.product_name = form.cleaned_data['product_name']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.sku = form.cleaned_data['sku']
            product.description = form.cleaned_data['product_description']
            product.brand = Brands.objects.filter(name = form.cleaned_data['brand_name'])
            product.category = Categories.objects.filter(name = form.cleaned_data['category_name'])
            product.save()
            messages.success(request,'Update profile successfully')
            return redirect('index')
    return render(request,'product/create-product.html',{'form':form})

@login_required
@user_passes_test(lambda user:user.is_staff)
def delete_product(request,id):
    product = Products.objects.filter(pk=id).first()
    product.delete()
    return redirect('index')

def get_product(request,id):
    product = Products.objects.filter(pk=id).first()
    if product is None:
        return render(request,'home/404.html')
    return render(request,'#',{'product':product})

def get_products(request):
    product_lists = Products.objects.all()
    return render(request,'#',{'products':product_lists})


#CRUD coupon(s)
@login_required
@user_passes_test(lambda user:user.is_active and user.is_staff and not user.is_superuser)
def create_coupon(request):
    form = CreateCouponForm()
    if request.method == 'POST':
        form = CreateCouponForm(request.POST)
        if Coupons.objects.filter(code = form.cleaned_data['code']).first():
            messages.error(request,'Code already existed')
        elif int(form.cleaned_data['minimum_purchase']) <=0:
            messages.error(request,'must be greateer than 0')
        else:
            coupon = Coupons.objects.create(code = form.cleaned_data['code'],
                                            description=form.cleaned_data['description'],
                                            discount_type=form.cleaned_data['discount_type'],
                                            discount_amount=form.cleaned_data['discount_amount'],
                                            minimum_purchase=form.cleaned_data['minimum_purchase'],
                                            expiration_date=form.cleaned_data['expiration_date'],
                                            usage_limit=form.cleaned_data['usage_limit'],
                                            status=COMMON_STATUS[0])
            coupon.save()
            return redirect('index')
        return redirect('createCoupon')
    return render(request,'#',{'form':form})

@login_required
@user_passes_test(lambda user:user.is_active and user.is_staff and not user.is_superuser)
def update_coupon(request,id):
    coupon = Coupons.objects.filter(pk = id).first()
    form = UpdateProductForm(initial={'code':coupon.code,
                                      'description': coupon.description,
                                      'discount_type':coupon.discount_type,
                                      'discount_amount':coupon.discount_amount,
                                      'minimum_purchase':coupon.minimum_purchase,
                                      'expiration_date':coupon.expiration_date,
                                      'usage_limit':coupon.usage_limit,
                                      'status':coupon.status})
    if request.method == 'POST':
        form = UpdateProductForm(request.POST)
        selected_coupon = Coupons.objects.filter(code = form.cleaned_data['code']).first()
        if selected_coupon and selected_coupon.code != coupon.code:
            messages.error(request,'Code already existed')
        elif int(form.cleaned_data['minimum_purchase']) <=0:
            messages.error(request,'must be greateer than 0')
        else:
            coupon.code = form.cleaned_data['code'],
            coupon.description=form.cleaned_data['description'],
            coupon.discount_type=form.cleaned_data['discount_type'],
            coupon.discount_amount=form.cleaned_data['discount_amount'],
            coupon.minimum_purchase=form.cleaned_data['minimum_purchase'],
            coupon.expiration_date=form.cleaned_data['expiration_date'],
            coupon.usage_limit=form.cleaned_data['usage_limit']
            coupon.status=form.cleaned_data['status']  
            coupon.save()
            return redirect('index')
        return redirect('createCoupon')
    return render(request,'#',{'form':form})

@login_required
@user_passes_test(lambda user:user.is_active and user.is_staff and not user.is_superuser)
def disable_coupon(request,id):
    coupon = Coupons.objects.filter(pk=id).first()
    if coupon is None:
        return render(request,'home/404.html')
    coupon.status = COMMON_STATUS[1]
    coupon.save()
    return render(request,'#')

@login_required
@user_passes_test(lambda user:user.is_active and user.is_staff and not user.is_superuser)
def enable_coupon(request,id):
    coupon = Coupons.objects.filter(pk=id).first()
    if coupon is None:
        return render(request,'home/404.html')
    coupon.status = COMMON_STATUS[0]
    coupon.save()
    return render(request,'#')

@login_required
@user_passes_test(lambda user:user.is_active and user.is_staff and not user.is_superuser)
def delete_coupon(request,id):
    coupon = Coupons.objects.filter(pk=id).first()
    if coupon is None:
        return render(request,'home/404.html')
    coupon.delete()
    return render(request,'#')


#CRUD 


# @login_required
# @user_passes_test(lambda user:not user.is_staff and not user.is_superuser)
# def add_to_cart(request,product_id):
#     user_id = request.user.id
#     product = Products.objects.filter(pk = product_id).first()
#     new_order = Orders.objects.create(user = Users.objects.filter(pk = user_id).first(),
#                                     #   order_date)
#                                         )
#     pass