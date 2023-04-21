from django.shortcuts import render, redirect,get_object_or_404

from django.contrib import messages
from .forms import LoginForm,SignUpForm,UpdateProfileForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# from .utils import send_email
from ecommerce_app.models import Users,ACCOUNT_STATUS


def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            if Users.objects.filter(username=username):
                messages.error(
                    request, 'This username is taken! Please log in instead!')
                return redirect('handleLogin')
            elif Users.objects.filter(email=email):
                messages.error(
                    request, 'This email is taken! Please log in instead!')
                return redirect('handleLogin')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password != confirm_password:
                messages.warning(
                    request, 'Confirm password must be the same with password!')
                return redirect('signUp')
            # send_email(email)
            user = Users.objects.create_user(
                username=username, email=email, password=password)
            user.account_status = ACCOUNT_STATUS[0]
            user.save()
            login(request, user)
            return redirect('index')

    return render(request, 'authentication/login-signup.html',{"form":form,"is_login":False})


def handle_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                if not Users.objects.filter(username = username).exists():
                    messages.error(request,"This account does not exist! Please Sign up first!")
                    return redirect('signUp')
                else:
                    messages.error(request,"Invalid password!")



    return render(request, 'authentication/login-signup.html',{"form":form,"is_login":True})

@login_required
def handle_logout(request):
    logout(request)
    return redirect('handleLogin')



@login_required
def update_profile(request):
    user_id = request.user.id
    user = get_object_or_404(Users,pk=user_id)
    form = UpdateProfileForm(initial={'username': user.username,
                                    'last_name': user.last_name,
                                    'first_name': user.first_name,
                                    'phone_number': user.phone_number,
                                    'gender': user.gender, 
                                    'DoB': user.date_of_birth,    
                                    'email': user.email,
                                    'subscription':user.newsletter_subscription,
                                    })
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone_number = form.cleaned_data['phone_number']
            user.gender = form.cleaned_data['gender']
            user.date_of_birth = form.cleaned_data['DoB']
            user.email = form.cleaned_data['email']
            user.newsletter_subscription = form.cleaned_data['subscription']
            user.profile_picture_url = form.cleaned_data['image']
            user.save()
            messages.success(request,'Update profile successfully')
            return redirect('updateProfile')

        
    return render(request, 'account/profile.html', {'form': form})

 