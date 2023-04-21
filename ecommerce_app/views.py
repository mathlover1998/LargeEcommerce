from django.shortcuts import render


def index(request):
    return render(request,'home/index.html')

def view_about_page(request):
    return render(request,'home/about.html')

def view_contact_page(request):
    return render(request,'home/contact.html')

def view_portfolio_detail_page(request):
    return render(request,'home/portfolio-details.html')

def view_service_page(request):
    return render(request,'home/service.html')

def view_privacy_policy_page(request):
    return render(request,'home/privacy-policy.html')

def test(request):
    return render(request,'foo/test.html')