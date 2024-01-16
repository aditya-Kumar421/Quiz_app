from rest_framework import serializers, validators
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True},
                        "email":{"required":True,
                                "allow_blank": False,
                                "validators":[
                                    validators.UniqueValidator(
                                        User.objects.all(),"A user with this Email already exists."
                                    )
                                ]
                            }
                    }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

