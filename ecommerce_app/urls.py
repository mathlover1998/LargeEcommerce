from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.view_about_page,name='viewAboutPage'),
    path('contact',views.view_contact_page,name='viewContactPage'),
    path('porfolio',views.view_portfolio_detail_page,name='viewPorfolio'),
    path('privacy-policy',views.view_privacy_policy_page,name='viewPrivacyPolicyPage'),
    path('service',views.view_service_page,name='viewServicePage'),
    path('test',views.test,name='test')
]