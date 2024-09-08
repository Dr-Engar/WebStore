from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_verified', 'is_locked')
    list_filter = ('is_staff', 'is_verified', 'is_locked')
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات اضافی', {'fields': ('phone_number', 'is_verified', 'is_locked', 'login_attempts')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('اطلاعات اضافی', {'fields': ('email', 'phone_number', 'is_verified')}),
    )
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)

    actions = ['verify_users', 'lock_users', 'unlock_users']

    def verify_users(self, request, queryset):
        queryset.update(is_verified=True)
    verify_users.short_description = "تأیید کاربران انتخاب شده"

    def lock_users(self, request, queryset):
        queryset.update(is_locked=True)
    lock_users.short_description = "قفل کردن کاربران انتخاب شده"

    def unlock_users(self, request, queryset):
        queryset.update(is_locked=False, login_attempts=0)
    unlock_users.short_description = "باز کردن قفل کاربران انتخاب شده"