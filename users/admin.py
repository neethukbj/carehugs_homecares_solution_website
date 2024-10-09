from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
	list_display=['name','city','phone_number']

@admin.register(Provider)
class ProviderModelAdmin(admin.ModelAdmin):
	list_display =['name','city','phone_number']
	
@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
	list_display=['user','is_provider','is_client']
