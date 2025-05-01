from django.contrib import admin
from .models import OTPValidation

@admin.register(OTPValidation)
class OTPValidation(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'student_no', 'otp', 'expired_at')
    list_filter = ('user_name','user_email', 'student_no', 'otp') 
    search_fields = ('user_name', 'user_email', 'student_no', 'otp')