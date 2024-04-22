from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import timedelta



class OTPValidation(models.Model):
    user_name = models.CharField(max_length = 30, blank = False)#
    user_email = models.EmailField(unique=True, blank = False)
    otp = models.CharField(max_length=6, unique = True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return f"OTP: {self.otp} - Email: {self.user_email}"

    def is_expired(self):
        return self.expired_at < timezone.now()
