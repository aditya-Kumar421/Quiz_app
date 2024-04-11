from django.db import models

class Mail(models.Model):
    email = models.EmailField(unique=True, blank = False)

    def __str__(self):
        return self.email

class OTPValidation(models.Model):
    user_email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP: {self.otp} - Email: {self.user_email}"
