from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[

    # Provider details and booking views
    path('provider/<int:provider_id>/', views.providerdetail, name='providerdetail'),
    path('booking/success/', views.booking_success_view, name='booking_success'),
    
    # Booking and payment views
    path('bookings/', views.bookings, name='bookings'),
    path('works/', views.works, name='works'),
    path('payments/', views.payments, name='payments'),
    path('complete-work/<int:booking_id>/', views.complete_work, name='complete_work'),
    path('confirm-work/<int:booking_id>/',views.confirm_work, name='confirm_work'),
    
    # Notification views
    path('notifications/', views.notifications, name='notifications'),
    path('provider_notifications/', views.provider_notifications, name='provider_notifications'),
   

]