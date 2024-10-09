from django.contrib import admin
from .models import *

admin.site.register(ServiceType)
#admin.site.register(BookingRequest)
admin.site.register(Message)

@admin.register(BookingRequest)
class BookingRequestModelAdmin(admin.ModelAdmin):
	list_display=['client_name','provider','booking_date','status','payment_status']
	list_filter = ('status', 'provider', 'service_type')
