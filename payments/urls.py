from django.urls import path
from .views import make_payment, payment_success

urlpatterns = [
    path('make_payment/', make_payment, name='make_payment'),
    path('payment_success/', payment_success, name='payment_success'),
]
