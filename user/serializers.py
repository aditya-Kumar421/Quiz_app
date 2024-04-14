from rest_framework import serializers, validators
from django.contrib.auth.models import User
from .models import OTPValidation

class OTPValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTPValidation
        fields = ('user_name','user_email', 'otp', 'created_at', 'expired_at')
        read_only_fields = ('created_at', 'expired_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        extra_kwargs = {"email":{"required":True,
                                "allow_blank": False,
                                "validators":[
                                    validators.UniqueValidator(
                                        User.objects.all(),"A user with this Email already exists."
                                    )
                                ]
                            }
                    }
    def validate_username(self, value):
        if ";" in value or "--" in value:
            raise serializers.ValidationError("Invalid username")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
