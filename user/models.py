from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_akgec_email(value):
        if not value.endswith('@akgec.ac.in'):
            raise ValidationError(
                _('Only college email id is allowed.'),
                params={'value': value},
            )
class Mail(models.Model):
    email = models.EmailField(max_length=40,validators=[validate_akgec_email], null=False, unique=True )

    def __str__(self):
        return self.email

class OTPValidation(models.Model):
    user_email = models.EmailField(max_length=40,validators=[validate_akgec_email], null=False, unique=True )
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP: {self.otp} - Email: {self.user_email}"
