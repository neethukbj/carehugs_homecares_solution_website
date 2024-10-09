from django.contrib import admin
from django.urls import path
from . import views
from services.views import *

urlpatterns =[

    #Home and common views
    path("",views.home,name="home"),
    path('entry/',views.entry,name="entry"),
    path("about/",views.aboutview,name="about"),
    path("contact/",views.contactview,name="contact"),
    path("serviceview/",views.serviceview,name="service"), 


    #Provider views
    path('signupprovider/',views.signupprovider,name="signupprovider"),
    path('providersignup/', views.providersignup, name="providersignup"),
    path('loginprovider/',views.loginprovider,name="loginprovider"),
    path('logoutprovider/',views.logoutprovider,name="logoutprovider"),
    path('providerdashboard/<int:user_profile_id>/', views.providerdashboard, name='providerdashboard'),
    path('providerdashboard/',views.providerdashboard,name="providerdashboard"),
    path('providerprofile/',views.providerprofile,name="providerprofile"),


    ####Client views
    path('signupclient/',views.signupclient,name="signupclient"),
    path('clientsignup/',views.clientsignup,name="clientsignup"),
    path('logoutclient/',views.logoutclient,name="logoutclient"),
    path('loginclient/',views.loginclient,name="loginclient"),


    #Provider listing and Payments

    path('allproviders/',views.allproviders,name="allproviders"),
    path('payment/<int:booking_id>/', views.payment_view, name='payment_view'),
    path('create-razorpay-order/<int:booking_id>/', views.create_razorpay_order, name='create_razorpay_order'),
    #path('create_razorpay_order/<int:booking_id>/', views.payment_view, name='create_razorpay_order'),
    

]