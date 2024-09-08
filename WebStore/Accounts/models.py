from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)
    
    # فیلدهای اضافی برای امنیت بیشتر
    last_password_change = models.DateTimeField(auto_now_add=True)
    login_attempts = models.PositiveIntegerField(default=0)
    is_locked = models.BooleanField(default=False)

    def __str__(self):
        return self.username