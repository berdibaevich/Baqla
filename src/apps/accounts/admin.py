from django.contrib import admin

from .models import UserBase



@admin.register(UserBase)
class UserBaseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'telegram_id', 
        'full_name', 
        'phone_number',
        'role', 
        'is_active', 
        'is_verified',
        'last_login'
    )

    list_editable = ('is_active', 'is_verified', 'role')
    search_fields = ('telegram_id', 'phone_number')
    list_filter = ('role', 'is_active', 'is_verified')